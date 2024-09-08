import { $, $doc, bodyOverflow } from './_utility';

/*------------------------------------------------------------------

  Init Plugin Fancybox

-------------------------------------------------------------------*/
function initPluginFancybox() {
  if (typeof $.fn.fancybox === 'undefined') {
    return;
  }

  $.fancybox.defaults.backFocus = false;

  $doc.on('beforeShow.fb', (e) => {
    bodyOverflow(1);

    setTimeout(() => {
      e.target.classList.add('flq-fancybox-open');
    }, 10);
  });

  $doc.on('afterClose.fb', () => {
    bodyOverflow(0);

    // Hide collapse.
    $('.flq-navbar-mobile .collapse').each(function () {
      const bsCollapse = new window.bootstrap.Collapse($(this)[0], {
        toggle: false,
      });

      bsCollapse.hide();
    });
  });

  $doc.on('keyup', (e) => {
    if (e.keyCode === 27) {
      $.fancybox.close();
    }
  });
}

export { initPluginFancybox };
