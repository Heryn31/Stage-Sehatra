import { throttle } from 'throttle-debounce';

import { $, $wnd, debounceResize } from './_utility';

/*------------------------------------------------------------------

  Init Images Ticker

-------------------------------------------------------------------*/
function initImagesTicker() {
  $('.flq-image-ticker').each(function () {
    const $ticker = $(this);
    const $tickerInner = $ticker.children();
    const $starterElements = $tickerInner.children('div');
    const gap = $ticker.attr('data-gap') || 20;
    const pixelsPerSecond = $ticker.attr('data-pixels-per-second') || 20;

    if (!$starterElements.length) {
      return;
    }

    if (gap) {
      $ticker.css('--flq-image-ticker__gap', `${gap}px`);
    }

    $starterElements.imagesLoaded(() => {
      let clonesCount = 1;
      let firstRun = true;

      // Create ticker clones if needed, recalculate animation speed.
      const recalculateTickerClones = throttle(200, () => {
        const wndW = $wnd.width();
        let clonesWidth = 0;

        $starterElements.each(function () {
          clonesWidth += $(this).innerWidth();
        });

        // We should fill the whole line + 2 more item to prevent possible blinking.
        const neededClones = 2 + Math.ceil(wndW / clonesWidth);

        if (neededClones > clonesCount) {
          const additionalClones = neededClones - clonesCount;

          for (let i = 0; i < additionalClones; i += 1) {
            $starterElements.clone().appendTo($tickerInner);
            clonesCount += 1;
          }
        }

        // Set animation.
        $tickerInner.css({
          width: clonesWidth,
          animationDuration: `${clonesWidth / pixelsPerSecond}s`,
        });

        // Show ticker on first run.
        if (firstRun) {
          firstRun = false;

          $ticker.addClass('flq-image-ticker-ready');
        }
      });

      debounceResize(recalculateTickerClones);
      recalculateTickerClones();
    });
  });
}

export { initImagesTicker };
