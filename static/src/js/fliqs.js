import { options } from './parts/_options';
import { debounceResize, throttleScroll, bodyOverflow, isInViewport } from './parts/_utility';
import { setOptions } from './parts/setOptions';
import { initCursor } from './parts/initCursor';
import { initNavbar } from './parts/initNavbar';
import { initDropdown } from './parts/initDropdown';
import { initAnchors } from './parts/initAnchors';
import { initForms } from './parts/initForms';
import { initImagesTicker } from './parts/initImagesTicker';
import { initBackgroundMove } from './parts/initBackgroundMove';
import { initScrollTopButton } from './parts/initScrollTopButton';
import { initScrollProgress } from './parts/initScrollProgress';
import { initOffcanvas } from './parts/initOffcanvas';
// plugins
import { initPluginScrollReveal } from './parts/initPluginScrollReveal';
import { initPluginRellax } from './parts/initPluginRellax';
import { initPluginSwiper } from './parts/initPluginSwiper';
import { initPluginAnime } from './parts/initPluginAnime';
import { initPluginObjectFitImages } from './parts/initPluginObjectFitImages';
import { initPluginCountUp } from './parts/initPluginCountUp';
import { initPluginIsotope } from './parts/initPluginIsotope';
import { initPluginFancybox } from './parts/initPluginFancybox';
import { initPluginTilt } from './parts/initPluginTilt';
import { initPluginJarallax } from './parts/initPluginJarallax';

/*------------------------------------------------------------------

  Fliqs Class

-------------------------------------------------------------------*/
class FLIQS {
  constructor() {
    this.options = options;
  }

  init() {
    // prt:sc:dm

    const self = this;
    self.initCursor();
    self.initNavbar();
    self.initDropdown();
    self.initAnchors();
    self.initForms();
    self.initImagesTicker();
    self.initBackgroundMove();
    self.initScrollTopButton();
    self.initScrollProgress();
    self.initOffcanvas();

    // init plugins
    self.initPluginScrollReveal();
    self.initPluginRellax();
    self.initPluginSwiper();
    self.initPluginAnime();
    self.initPluginObjectFitImages();
    self.initPluginCountUp();
    self.initPluginIsotope();
    self.initPluginFancybox();
    self.initPluginTilt();
    self.initPluginJarallax();

    const tooltip = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltip.map((tooltipTriggerEl) => new window.bootstrap.Tooltip(tooltipTriggerEl));

    const popover = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popover.map((popoverTriggerEl) => new window.bootstrap.Popover(popoverTriggerEl));

    return self;
  }

  setOptions(newOpts) {
    return setOptions.call(this, newOpts);
  }

  debounceResize(func) {
    return debounceResize.call(this, func);
  }

  throttleScroll(callback) {
    return throttleScroll.call(this, callback);
  }

  bodyOverflow(type) {
    return bodyOverflow.call(this, type);
  }

  isInViewport($item, returnRect) {
    return isInViewport.call(this, $item, returnRect);
  }

  initCursor() {
    return initCursor.call(this);
  }

  initNavbar() {
    return initNavbar.call(this);
  }

  initDropdown() {
    return initDropdown.call(this);
  }

  initAnchors() {
    return initAnchors.call(this);
  }

  initForms() {
    return initForms.call(this);
  }

  initImagesTicker() {
    return initImagesTicker.call(this);
  }

  initBackgroundMove() {
    return initBackgroundMove.call(this);
  }

  initScrollTopButton() {
    return initScrollTopButton.call(this);
  }

  initScrollProgress() {
    return initScrollProgress.call(this);
  }

  initOffcanvas() {
    return initOffcanvas.call(this);
  }

  initPluginScrollReveal() {
    return initPluginScrollReveal.call(this);
  }

  initPluginRellax() {
    return initPluginRellax.call(this);
  }

  initPluginSwiper() {
    return initPluginSwiper.call(this);
  }

  initPluginAnime() {
    return initPluginAnime.call(this);
  }

  initPluginObjectFitImages() {
    return initPluginObjectFitImages.call(this);
  }

  initPluginCountUp() {
    return initPluginCountUp.call(this);
  }

  initPluginIsotope() {
    return initPluginIsotope.call(this);
  }

  initPluginFancybox() {
    return initPluginFancybox.call(this);
  }

  initPluginTilt() {
    return initPluginTilt.call(this);
  }

  initPluginJarallax() {
    return initPluginJarallax.call(this);
  }
}

/*------------------------------------------------------------------

  Init Fliqs

-------------------------------------------------------------------*/
window.Fliqs = new FLIQS();
