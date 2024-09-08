import { $, $doc, $body, isMobile } from './_utility';

/*------------------------------------------------------------------

  Cursor

-------------------------------------------------------------------*/
function initCursor() {
  const self = this;
  const $swiper = $('.swiper');

  if (isMobile || !$swiper.length || !self.options.customCursor) {
    return;
  }

  let clientX = 0;
  let clientY = 0;
  let xPos = 0;
  let yPos = 0;
  const delay = 1.5;

  // Add cursor.
  const $cursor = $('<div class="flq-cursor"><span></span></div>');

  $body.append($cursor).addClass('flq-cursor-enabled');
  $cursor.wrapAll('<div></div>');

  // Show / hide.
  const classShow = 'flq-cursor-show';
  $doc
    // Add class when hover on slider.
    .on('mouseenter', '.swiper', () => {
      $cursor.addClass(classShow);
    })
    // Remove class when hover on slider.
    .on('mouseleave', '.swiper', () => {
      $cursor.removeClass(classShow);
    })
    // Add class when hover on links.
    .on('mouseleave', '.swiper .btn, .swiper .flq-meta a', () => {
      $cursor.addClass(classShow);
    })
    // Remove class when hover on links.
    .on('mouseenter', '.swiper .btn, .swiper .flq-meta a', () => {
      $cursor.removeClass(classShow);
    });

  // Move cursor.
  $doc.on('mousemove drag', (e) => {
    clientX = e.clientX;
    clientY = e.clientY;
  });

  const moveCursor = () => {
    xPos += (clientX - xPos) / delay;
    yPos += (clientY - yPos) / delay;

    $cursor.css('transform', `matrix(1, 0, 0, 1, ${xPos}, ${yPos}) translate3d(0,0,0)`);

    requestAnimationFrame(moveCursor);
  };

  requestAnimationFrame(moveCursor);
}

export { initCursor };
