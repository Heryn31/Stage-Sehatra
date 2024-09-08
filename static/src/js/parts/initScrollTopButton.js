import { $, $doc, isMobile, throttleScroll } from './_utility';

/*------------------------------------------------------------------

  Scroll top button

-------------------------------------------------------------------*/
function initScrollTopButton() {
  const $button = $('.flq-scroll-top-wrapper');
  const buttonClassShow = 'flq-scroll-top-button-show';
  const buttonClassHide = 'flq-scroll-top-button-hide';

  if (!$button.length) {
    return;
  }

  // show / hide.
  throttleScroll((type, scroll) => {
    if (type === 'end' || scroll > 400) {
      $button.addClass(buttonClassShow);
    } else {
      $button.removeClass(buttonClassShow);
    }
  });

  // Hide navbar-icons when open keyboard.
  if (isMobile) {
    $doc.on('focus', 'select, input, textarea', () => {
      $button.addClass(buttonClassHide);
    });

    $doc.on('blur', 'select, input, textarea', () => {
      $button.removeClass(buttonClassHide);
    });
  }
}

export { initScrollTopButton };
