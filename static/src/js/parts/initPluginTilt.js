import { $ } from './_utility';

/*------------------------------------------------------------------

  Tilt

-------------------------------------------------------------------*/
function initPluginTilt() {
  const { VanillaTilt } = window;

  if (typeof VanillaTilt === 'undefined') {
    return;
  }

  $('.flq-card-feature-filled, .flq-card-movie, .flq-card-pricing').each(function () {
    const $this = $(this);
    const conf = {};

    if ($this.parents('.swiper-slide').length) {
      return;
    }

    conf.max = 4;
    conf.speed = 1000;

    VanillaTilt.init($this[0], conf);
  });
}

export { initPluginTilt };
