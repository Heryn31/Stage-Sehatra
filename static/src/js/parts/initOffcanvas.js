import { $, $body } from './_utility';

/*------------------------------------------------------------------

  Offcanvas

-------------------------------------------------------------------*/
function initOffcanvas() {
  $('.offcanvas').each(function () {
    const $this = $(this);
    const classClosing = 'flq-offcanvas-is-closing';
    const classBodyActive = 'flq-offcanvas-active';

    $this[0].addEventListener('show.bs.offcanvas', () => {
      $body.addClass(classBodyActive);
    });
    $this[0].addEventListener('hide.bs.offcanvas', () => {
      $this.addClass(classClosing);
    });
    $this[0].addEventListener('hidden.bs.offcanvas', () => {
      $this.removeClass(classClosing);

      if (!$('.offcanvas').hasClass('show')) {
        $body.removeClass(classBodyActive);
      }
    });
  });
}

export { initOffcanvas };
