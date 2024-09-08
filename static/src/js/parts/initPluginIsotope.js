import { $, $doc } from './_utility';

/*------------------------------------------------------------------

  Isotope

-------------------------------------------------------------------*/
function initPluginIsotope() {
  if (typeof $.fn.isotope === 'undefined') {
    return;
  }

  $('.flq-isotope').each(function () {
    const $this = $(this);
    const $grid = $this.find('.flq-isotope-grid');
    const curIsotopeOptions = $this.find('.flq-isotope-options');
    const dataLayout = $grid.attr('data-isotope-layout');
    const conf = {};

    conf.itemSelector = '.flq-isotope-item';

    if (dataLayout) {
      conf.layoutMode = dataLayout;
    }

    // init items
    const isotope = $grid.isotope(conf);

    // refresh for parallax images and isotope images position
    if (isotope.imagesLoaded) {
      $doc.imagesLoaded().progress(() => {
        isotope.isotope('layout');
      });
    }

    // click on filter button
    curIsotopeOptions.on('click', '> li > :not(.active)', function (e) {
      // eslint-disable-next-line newline-per-chained-call
      $(this).addClass('active').parent().siblings().children().removeClass('active');
      const curFilter = $(this).attr('data-filter');

      e.preventDefault();

      isotope.isotope({
        filter() {
          if (curFilter === 'all') {
            return true;
          }

          let itemFilters = $(this).attr('data-filters');

          if (itemFilters) {
            itemFilters = itemFilters.split(',');
            // eslint-disable-next-line
            for (const k in itemFilters) {
              if (itemFilters[k].replace(/\s/g, '') === curFilter) {
                return true;
              }
            }
          }
          return false;
        },
      });
    });
  });
}

export { initPluginIsotope };
