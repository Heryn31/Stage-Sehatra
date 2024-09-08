import { $, isMobile } from './_utility';

/*------------------------------------------------------------------

  Jarallax

-------------------------------------------------------------------*/
function initPluginJarallax() {
  if (!this.options.parallax || isMobile) {
    return;
  }

  // in newest versions used Jarallax plugin
  if (typeof $.fn.jarallax === 'undefined') {
    return;
  }

  $('.jarallax').each(function () {
    const speed = parseFloat($(this).attr('data-speed'));

    $(this).jarallax({
      speed: Number.isNaN(speed) ? 0.4 : speed,
    });
  });
}

export { initPluginJarallax };
