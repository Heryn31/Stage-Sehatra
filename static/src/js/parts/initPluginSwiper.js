import { $ } from './_utility';

/*------------------------------------------------------------------

  Init Plugin Swiper

-------------------------------------------------------------------*/
function initPluginSwiper() {
  const { Swiper } = window;

  if (typeof Swiper === 'undefined') {
    return;
  }

  // Search swiper elements.
  function searchSwiperElement($wrapper, $this, elementClass) {
    return $wrapper.length ? $wrapper.find(elementClass) : $this.find(elementClass);
  }

  // Add zero before number.
  function addZeroBeforeNumber(number) {
    return number <= 9 ? `0${number}` : number;
  }

  // Add attribute bullets total.
  function addAttrBulletsTotal($pagination, element) {
    $pagination.attr('data-bullets-total', addZeroBeforeNumber(element.snapGrid.length));
  }

  const $cursor = $('.flq-cursor');

  $('.swiper').each(function () {
    const $this = $(this);
    const $wrapper = $this.parents('.flq-swiper-wrapper');
    const classBtnNext = '.flq-swiper-button-next';
    const classBtnPrev = '.flq-swiper-button-prev';
    const classPagination = '.flq-swiper-pagination';
    const classPaginationProgress = '.flq-swiper-pagination-progress';

    const dataButtons = $this.attr('data-buttons');
    const dataPagination = $this.attr('data-pagination');
    const dataPaginationDynamic = $this.attr('data-pagination-dynamic');
    const dataPaginationProgress = $this.attr('data-pagination-progress');
    const dataLoop = $this.attr('data-loop');
    const dataGrabCursor = $this.attr('data-grab-cursor');
    const dataParallax = $this.attr('data-parallax');
    const dataFreeMode = $this.attr('data-free-mode');
    const dataAutoHeight = $this.attr('data-auto-height');
    const dataBreakpoints = $this.attr('data-breakpoints');
    const dataSlides = $this.attr('data-slides');
    const dataTouchRatio = parseFloat($this.attr('data-touch-ratio'));
    const dataAutoplay = parseInt($this.attr('data-autoplay'), 10);
    const dataSpeed = parseInt($this.attr('data-speed'), 10);
    const dataGap = parseInt($this.attr('data-gap'), 10);
    const conf = {};

    // fix the conflict with custom cursor movement.
    conf.touchStartPreventDefault = false;

    // fix touch in the spacebetween when move cursor.
    conf.touchEventsTarget = 'container';

    // Options.
    conf.loop = dataLoop ? true : '';
    conf.freeMode = dataFreeMode ? true : '';
    conf.parallax = dataParallax ? true : '';
    conf.grabCursor = dataGrabCursor ? true : '';
    conf.autoHeight = dataAutoHeight ? true : '';
    conf.touchRatio = dataTouchRatio || 1;
    conf.speed = dataSpeed || 400;
    conf.spaceBetween = dataGap || 0;
    conf.autoplay = dataAutoplay ? { delay: dataAutoplay } : false;
    conf.slidesPerView = dataSlides >= 1 ? parseInt(dataSlides, 10) : 1;
    conf.keyboard = {
      enabled: true,
    };

    // Buttons.
    if (dataButtons) {
      const $btnNext = searchSwiperElement($wrapper, $this, classBtnNext);
      const $btnPrev = searchSwiperElement($wrapper, $this, classBtnPrev);

      conf.navigation = {
        nextEl: $btnNext[0],
        prevEl: $btnPrev[0],
        disabledClass: 'disabled',
      };
    }

    // Pagination.
    if (dataPagination) {
      const $pagination = searchSwiperElement($wrapper, $this, classPagination);

      conf.pagination = {
        el: $pagination[0],
        dynamicBullets: dataPaginationDynamic ? true : '',
        clickable: true,
      };
    }

    // Pagination Progress.
    if (dataPaginationProgress) {
      const $pagination = searchSwiperElement($wrapper, $this, classPaginationProgress);

      conf.pagination = {
        el: $pagination[0],
        type: 'progressbar',
      };
    }

    // Breakpoints.
    if (dataBreakpoints) {
      let i = 0;
      const breaks = {};
      const points = dataBreakpoints.split(',');
      while (i < dataBreakpoints.split(',').length) {
        breaks[parseInt(points[i].split(':')[0], 10)] = {
          slidesPerView: parseInt(points[i].split(':')[1], 10),
        };
        i += 1;
      }
      conf.breakpoints = breaks;
    }

    // Add class "touch" when touch mouse.
    conf.on = {
      touchStart: (e) => {
        const $slider = e.$el.parent();

        if ($slider.hasClass('flq-swiper-effect-touch')) {
          $slider.addClass('flq-swiper-touch');
        }
        if ($cursor.length) {
          $cursor.addClass('flq-cursor-touch');
        }
      },

      touchEnd: (e) => {
        const $slider = e.$el.parent();

        if ($slider.hasClass('flq-swiper-effect-touch')) {
          $slider.removeClass('flq-swiper-touch');
        }
        if ($cursor.length) {
          $cursor.removeClass('flq-cursor-touch');
        }
      },

      slideNextTransitionStart: () => {
        $this.children().trigger('swiperSlideNextTransitionStart');
      },
      slidePrevTransitionStart: () => {
        $this.children().trigger('swiperSlidePrevTransitionStart');
      },
      activeIndexChange: () => {
        $this.children().trigger('swiperActiveIndexChange');
      },
    };

    // eslint-disable-next-line
    new Swiper($this.children()[0], conf);
  });

  // Pagination custom.
  $('.swiper-container').each(function () {
    const self = this;
    const $this = $(self);
    const $wrapper = $this.parents('.flq-swiper-wrapper');
    const classPaginationCustom = '.flq-swiper-pagination-custom';
    const classBulletActive = 'swiper-pagination-bullet-active';
    const thisSwiper = self.swiper;
    const slides = thisSwiper.slides.length;

    const $pagination = searchSwiperElement($wrapper, $this, classPaginationCustom);

    // Added bullets.
    for (let index = 0; index < slides; index += 1) {
      $pagination.append(
        `<span class="swiper-pagination-bullet">${addZeroBeforeNumber(index + 1)}</span>`
      );
    }

    // Added active class in the first bullet.
    $($pagination.children()[0]).addClass(classBulletActive);

    // Added attribute total bullets.
    addAttrBulletsTotal($pagination, thisSwiper);

    thisSwiper.on('snapGridLengthChange', () => {
      addAttrBulletsTotal($pagination, thisSwiper);
    });

    // Toggle active class in the bullets.
    thisSwiper.on('slideChange', (e) => {
      $pagination.children().removeClass(classBulletActive);
      $($pagination.children()[e.activeIndex]).addClass(classBulletActive);
    });
  });
}

export { initPluginSwiper };
