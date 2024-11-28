import { $, isMobile, $doc, throttleScroll } from './_utility';

/*------------------------------------------------------------------

  Navbar

-------------------------------------------------------------------*/
function initNavbar() {
  const $navbarTop = $('.flq-navbar-top');
  const $navbarIcons = $('.flq-navbar-icons');
  const navbarTopClassHide = 'flq-navbar-top-hide';
  const navbarTopClassScroll = 'flq-navbar-top-scroll';
  const navbarIconsClassEnd = 'flq-navbar-icons-end';
  const navbarIconsClassHide = 'flq-navbar-icons-hide';

  throttleScroll((type, scroll) => {
    // Add class show or hide in the navbar-top.
    if (type === 'down' && scroll > 500) {
      $navbarTop.addClass(navbarTopClassHide);
    } else if (type === 'up' || type === 'start') {
      $navbarTop.removeClass(navbarTopClassHide);
    }

    // Add scroll class in the navbar-top.
    if (scroll > 100) {
      $navbarTop.addClass(navbarTopClassScroll);
    } else {
      $navbarTop.removeClass(navbarTopClassScroll);
    }

    // Hide navbar icons when scroll end.
    if (type === 'end') {
      $navbarIcons.addClass(navbarIconsClassEnd);
    } else {
      $navbarIcons.removeClass(navbarIconsClassEnd);
    }
  });

  // Hide navbar-icons when open keyboard.
  if (isMobile) {
    $doc.on('focus', 'select, input:not([type="checkbox"]):not([type="radio"]), textarea', () => {
      $navbarIcons.addClass(navbarIconsClassHide);
    });

    $doc.on('blur', 'select, input:not([type="checkbox"]):not([type="radio"]), textarea', () => {
      $navbarIcons.removeClass(navbarIconsClassHide);
    });
  }
}

export { initNavbar };
