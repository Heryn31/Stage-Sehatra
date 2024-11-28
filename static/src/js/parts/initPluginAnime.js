import { $doc } from './_utility';

/*------------------------------------------------------------------

  Init Plugin Animejs

-------------------------------------------------------------------*/
function initPluginAnime() {
  const { anime } = window;

  if (typeof anime === 'undefined') {
    return;
  }

  // Preloader title.
  const preloaderTitle = anime({
    easing: 'easeOutSine',
    duration: 400,
    translateX: ['100%', 0],
    targets: '.flq-preloader .flq-preloader-title > span',
    'clip-path': ['inset(0 100% 0 0)', 'inset(0 0% 0 0)'],
    autoplay: false,
    delay: anime.stagger(50, { start: 0 }),
  });

  // Card team social.
  let cardTeamSocial;

  $doc.on('mouseenter', '.flq-card-team', (e) => {
    cardTeamSocial = anime({
      easing: 'cubicBezier(0.2, 1, 0.2, 1)',
      duration: 700,
      opacity: [0, 1],
      translateY: ['100%', 0],
      targets: e.currentTarget.querySelectorAll('.flq-social li a'),
      autoplay: false,
      delay: anime.stagger(80, { start: 0 }),
    });

    cardTeamSocial.play();
  });

  $doc.on('mouseleave', '.flq-card-team', () => {
    cardTeamSocial.reverse();
    cardTeamSocial.play();
  });

  // Search social show.
  const searchSocialShow = anime({
    easing: 'easeOutSine',
    duration: 300,
    opacity: [0, 1],
    translateY: ['100%', 0],
    targets: '.flq-search .flq-social li',
    autoplay: false,
    delay: anime.stagger(80, { start: 500 }),
  });

  // Search social close.
  const searchSocialClose = anime({
    easing: 'easeOutSine',
    duration: 300,
    opacity: [1, 0],
    translateY: [0, '100%'],
    targets: '.flq-search .flq-social li',
    autoplay: false,
    delay: anime.stagger(80, { start: 0 }),
  });

  // Navbar mobile show.
  const navbarMobileShow = anime({
    easing: 'cubicBezier(0.2, 1, 0.2, 1)',
    duration: 1100,
    translateY: ['60%', 0],
    targets:
      '.flq-navbar-mobile .flq-fancybox-body > .nav > .nav-item, .flq-navbar-mobile .flq-fancybox-body > div > .nav > .nav-item',
    'clip-path': ['inset(0 -100% 100% -100%)', 'inset(0 -100% 0% -100%)'],
    autoplay: false,
    delay: anime.stagger(80, { start: 160 }),
  });

  // Navbar mobile close.
  const navbarMobileClose = anime({
    easing: 'cubicBezier(0.2, 1, 0.2, 1)',
    duration: 1500,
    translateY: [0, '60%'],
    targets:
      '.flq-navbar-mobile .flq-fancybox-body > .nav > .nav-item, .flq-navbar-mobile .flq-fancybox-body > div > .nav > .nav-item',
    'clip-path': ['inset(0 -100% 0% -100%)', 'inset(0 -100% 100% -100%)'],
    autoplay: false,
  });

  // Navbar mobile widgets show.
  const navbarMobileWidgetsShow = anime({
    easing: 'easeOutSine',
    duration: 400,
    opacity: [0, 1],
    translateY: ['30px', 0],
    targets: '.flq-navbar-mobile .flq-sidebar .flq-widget',
    autoplay: false,
    delay: anime.stagger(80, { start: 300 }),
  });

  // Navbar mobile widgets close.
  const navbarMobileWidgetsClose = anime({
    easing: 'easeOutSine',
    duration: 400,
    opacity: [1, 0],
    translateY: [0, '30px'],
    targets: '.flq-navbar-mobile .flq-sidebar .flq-widget',
    autoplay: false,
  });

  preloaderTitle.play();

  $doc.on('beforeShow.fb', () => {
    navbarMobileShow.play();
    navbarMobileWidgetsShow.play();
    searchSocialShow.play();
  });

  $doc.on('beforeClose.fb', () => {
    navbarMobileClose.play();
    navbarMobileWidgetsClose.play();
    searchSocialClose.play();
  });

  // Main slider.
  const classSwiperMain = '.flq-swiper-main .swiper-container';
  let swiperMainTranslate;

  $doc.on('swiperSlideNextTransitionStart', classSwiperMain, () => {
    swiperMainTranslate = ['40px', 0];
  });

  $doc.on('swiperSlidePrevTransitionStart', classSwiperMain, () => {
    swiperMainTranslate = ['-40px', 0];
  });

  $doc.on('swiperActiveIndexChange', classSwiperMain, () => {
    setTimeout(() => {
      anime({
        easing: 'easeOutCubic',
        duration: 600,
        opacity: [0, 1],
        translateX: swiperMainTranslate,
        targets: '.flq-swiper-main .swiper-slide-active [data-animejs]',
        autoplay: true,
        delay: anime.stagger(35, { start: 280 }),
      });
    }, 10);
  });

  $doc.on('flq.preloader.hide', () => {
    anime({
      easing: 'easeInOutCubic',
      duration: 700,
      opacity: [0, 1],
      translateY: ['15px', 0],
      targets: '.flq-swiper-main .swiper-slide-active [data-animejs]',
      autoplay: true,
      delay: anime.stagger(50, { start: 700 }),
    });

    anime({
      easing: 'easeOutCubic',
      duration: 800,
      opacity: [0, 1],
      scale: [1.15, 1],
      targets: '.flq-swiper-main .swiper-slide-active .flq-background-image',
      autoplay: true,
      delay: 800,
    });
  });
}

export { initPluginAnime };
