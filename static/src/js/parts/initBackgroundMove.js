import { $, $doc } from './_utility';

function initBackgroundMove() {
  let cursorX = 0;
  let cursorY = 0;
  let delayX = 0;
  let delayY = 0;
  const delay = 200;
  const maxMove = 30;

  const $backgroundImage = $('.flq-background-move > .flq-background-image > .flq-image');
  $backgroundImage.css({
    top: -maxMove,
    right: -maxMove,
    bottom: -maxMove,
    left: -maxMove,
  });

  $doc.on('mousemove drag', (e) => {
    cursorX = e.clientX;
    cursorY = e.clientY;
  });

  function moveBackgroundImage() {
    const wndW = window.innerWidth / 2;
    const wndH = window.innerHeight / 2;
    const xPos = -((cursorX - wndW) / wndW) * maxMove;
    const yPos = -((cursorY - wndH) / wndH) * maxMove;

    delayX += (xPos - delayX) / delay;
    delayY += (yPos - delayY) / delay;

    $backgroundImage.css(
      'transform',
      `matrix(1, 0, 0, 1, ${delayX}, ${delayY}) translate3d(0,0,0)`
    );

    requestAnimationFrame(moveBackgroundImage);
  }

  requestAnimationFrame(moveBackgroundImage);
}

export { initBackgroundMove };
