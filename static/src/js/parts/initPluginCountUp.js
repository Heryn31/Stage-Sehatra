import { CountUp } from 'countup.js';

import { $, isInViewport, throttleScroll } from './_utility';

/*------------------------------------------------------------------

  Init CountUp

-------------------------------------------------------------------*/

function initPluginCountUp() {
  if (typeof CountUp === 'undefined') {
    return;
  }

  throttleScroll(() => {
    $('.flq-count:not(.flq-count-stop)').each(function () {
      const $this = $(this);
      const number = parseInt($this.text(), 10);
      const conf = {};

      if (isInViewport($this) > 0) {
        conf.useGrouping = false;
        conf.duration = 3;

        const countUp = new CountUp($this[0], number, conf);

        countUp.start();
        $this.addClass('flq-count-stop');
      }
    });
  });
}

export { initPluginCountUp };
