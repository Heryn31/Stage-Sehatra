import { $, $doc } from './_utility';

function initPluginScrollReveal() {
  const { ScrollReveal } = window;

  if (typeof ScrollReveal === 'undefined') {
    return;
  }

  $doc.on('flq.preloader.hide', () => {
    setTimeout(() => {
      $('[data-sr]').each(function () {
        const $this = $(this);
        const dataId = $this.attr('data-sr') || '';
        const dataInterval = parseInt($this.attr('data-sr-interval'), 10);
        const dataDuration = parseInt($this.attr('data-sr-duration'), 10);
        const dataDelay = parseInt($this.attr('data-sr-delay'), 10);
        const dataScale = parseFloat($this.attr('data-sr-scale'));
        const dataOrigin = $this.attr('data-sr-origin');
        const dataDistance = $this.attr('data-sr-distance');
        const conf = {};
        const $item = $this.find(`[data-sr-item="${dataId}"]`).length
          ? $this.find(`[data-sr-item="${dataId}"]`)
          : $this;

        conf.reset = true;
        conf.cleanup = true;
        conf.reset = false;
        conf.interval = dataInterval || 1;
        conf.duration = dataDuration || 100;
        conf.delay = dataDelay || 0;
        conf.scale = dataScale || 1;
        conf.origin = dataOrigin || 'bottom';
        conf.distance = dataDistance ? `${dataDistance}px` : 0;

        ScrollReveal().reveal($item, conf);
      });

      $doc.on('arrangeComplete', '.flq-isotope-grid', () => {
        ScrollReveal().delegate({ type: 'resize' });
      });
    }, 500);
  });
}

export { initPluginScrollReveal };
