import rafSchd from 'raf-schd';

import { $, $wnd, throttleScroll } from './_utility';

/*------------------------------------------------------------------

  Scroll top button

-------------------------------------------------------------------*/
function initScrollProgress() {
  const $progress = $('.flq-scroll-progress');

  function updateScrollProgress() {
    const maxHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrollProgress = Math.min(100, ($wnd.scrollTop() / maxHeight) * 100).toFixed(2);

    $progress.each(function () {
      this.style.setProperty('--flq-scroll-progress', `${scrollProgress}%`);
    });
  }

  if ($progress.length) {
    $wnd.on('scroll resize', rafSchd(updateScrollProgress));
    $(rafSchd(updateScrollProgress));

    throttleScroll((type, scroll) => {
      if (type === 'end' || scroll > 400) {
        // Display progress bar only if document height is twice larger than window height.
        if (window.innerHeight * 2 < document.documentElement.offsetHeight) {
          $progress.addClass('flq-scroll-progress-show');
        }
      } else {
        $progress.removeClass('flq-scroll-progress-show');
      }
    });
  }
}

export { initScrollProgress };
