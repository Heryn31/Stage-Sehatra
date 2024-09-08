/*------------------------------------------------------------------

  Utility

-------------------------------------------------------------------*/
import { throttle } from 'throttle-debounce';
import rafSchd from 'raf-schd';

const $ = window.jQuery;
const isIos =
  ['iPad Simulator', 'iPhone Simulator', 'iPod Simulator', 'iPad', 'iPhone', 'iPod'].includes(
    navigator.platform
  ) ||
  (navigator.userAgent.includes('Mac') && 'ontouchend' in document);

const isMobile =
  isIos ||
  /Android|BlackBerry|Windows Phone/g.test(navigator.userAgent || navigator.vendor || window.opera);

/**
 * window size
 */
const $wnd = $(window);
const $doc = $(document);
const $body = $('body');
const $html = $('html');

// add 'is-mobile' or 'is-desktop' classname to html tag
$html.addClass(isMobile ? 'is-mobile' : 'is-desktop');

if (isIos) {
  $html.addClass('is-ios');
}

/**
 * Debounce resize
 */
const resizeArr = [];
function debounceResized() {
  if (resizeArr.length) {
    for (let k = 0; k < resizeArr.length; k += 1) {
      resizeArr[k]();
    }
  }
}
$wnd.on('load resize orientationchange', throttle(200, rafSchd(debounceResized)));
$(rafSchd(debounceResized));
debounceResized();

function debounceResize(func) {
  if (typeof func === 'function') {
    resizeArr.push(func);
  } else {
    window.dispatchEvent(new Event('resize'));
  }
}

/**
 * Throttle scroll
 */
const hideOnScrollList = [];
let lastST = 0;

function hasScrolled() {
  if (!hideOnScrollList.length) {
    return;
  }

  const ST = $wnd.scrollTop();

  let type = ''; // [up, down, end, start]

  if (ST > lastST) {
    type = 'down';
  } else if (ST < lastST) {
    type = 'up';
  } else {
    type = 'none';
  }

  if (ST === 0) {
    type = 'start';
  } else if (window.innerHeight + window.scrollY >= document.body.scrollHeight) {
    type = 'end';
  }

  hideOnScrollList.forEach((value) => {
    if (typeof value === 'function') {
      value(type, ST, lastST, $wnd);
    }
  });

  lastST = ST;
}

$wnd.on('scroll load resize orientationchange', throttle(200, rafSchd(hasScrolled)));
$(rafSchd(hasScrolled));

function throttleScroll(callback) {
  hideOnScrollList.push(callback);
}

/**
 * Body Overflow
 * Thanks https://jsfiddle.net/mariusc23/s6mLJ/31/
 * Usage:
 *    // enable
 *    bodyOverflow(1);
 *
 *    // disable
 *    bodyOverflow(0);
 */
let bodyOverflowEnabled;
let isBodyOverflowing;
let scrollbarWidth;
let originalBodyStyle;
const originalBodyPadding = parseFloat($body.css('margin-right')) || 0;
function bodyGetScrollbarWidth() {
  // thx d.walsh
  const scrollDiv = document.createElement('div');
  scrollDiv.className = 'body-scrollbar-measure';
  $body[0].appendChild(scrollDiv);
  const result = scrollDiv.offsetWidth - scrollDiv.clientWidth;
  $body[0].removeChild(scrollDiv);
  return result;
}
function bodyCheckScrollbar() {
  let fullWindowWidth = window.innerWidth;
  if (!fullWindowWidth) {
    // workaround for missing window.innerWidth in IE8
    const documentElementRect = document.documentElement.getBoundingClientRect();
    fullWindowWidth = documentElementRect.right - Math.abs(documentElementRect.left);
  }
  isBodyOverflowing = $body[0].clientWidth < fullWindowWidth;

  scrollbarWidth = isBodyOverflowing ? bodyGetScrollbarWidth() : 0;
}
function bodySetScrollbar() {
  if (typeof originalBodyStyle === 'undefined') {
    originalBodyStyle = $body.attr('style') || '';
  }

  if (isBodyOverflowing) {
    $body.css('margin-right', scrollbarWidth + originalBodyPadding);
  }
}
function bodyResetScrollbar() {
  $body.attr('style', originalBodyStyle);
}
function bodyOverflow(enable) {
  if (enable && !bodyOverflowEnabled) {
    bodyOverflowEnabled = 1;
    bodyCheckScrollbar();
    bodySetScrollbar();
    $body.css('overflow', 'hidden');
  } else if (!enable && bodyOverflowEnabled) {
    bodyOverflowEnabled = 0;
    $body.css('overflow', '');
    bodyResetScrollbar();
  }
}

// Set scrollbar size variable.
function updateScrollbarVariable() {
  bodyCheckScrollbar();

  $body[0].style.setProperty('--flq-page-scrollbar__size', `${scrollbarWidth}px`);
}
$wnd.on('load resize', rafSchd(updateScrollbarVariable));
$(rafSchd(updateScrollbarVariable));
updateScrollbarVariable();

/**
 * In Viewport checker
 * return visible percent from 0 to 1
 */
function isInViewport($item, returnRect) {
  const rect = $item[0].getBoundingClientRect();
  const wndH = window.innerHeight;
  let result = 1;

  if (rect.right <= 0 || rect.left >= window.innerWidth) {
    result = 0;
  } else if (rect.bottom < 0 && rect.top <= wndH) {
    result = 0;
  } else {
    const beforeTopEnd = Math.max(0, rect.height + rect.top);
    const beforeBottomEnd = Math.max(0, rect.height - (rect.top + rect.height - wndH));
    const afterTop = Math.max(0, -rect.top);
    const beforeBottom = Math.max(0, rect.top + rect.height - wndH);
    if (rect.height < wndH) {
      result = 1 - (afterTop || beforeBottom) / rect.height;
    } else if (beforeTopEnd <= wndH) {
      result = beforeTopEnd / wndH;
    } else if (beforeBottomEnd <= wndH) {
      result = beforeBottomEnd / wndH;
    }
    result = result < 0 ? 0 : result;
  }
  if (returnRect) {
    return [result, rect];
  }
  return result;
}

export {
  $,
  isIos,
  isMobile,
  $wnd,
  $doc,
  $html,
  $body,
  debounceResize,
  throttleScroll,
  bodyOverflow,
  isInViewport,
};
