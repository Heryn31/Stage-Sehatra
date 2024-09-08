import { $, $doc, $wnd, debounceResize } from './_utility';

/*------------------------------------------------------------------

  Dropdown

-------------------------------------------------------------------*/
function initDropdown() {
  // Dropdown
  const $itemDropdown = $('.flq-dropdown');
  const $dropdownMenu = $itemDropdown.children('.dropdown-menu');

  // closing the menu when click to the side
  $doc.on('mouseup', (e) => {
    const dropdownHas = $itemDropdown.has(e.target).length;

    if (!dropdownHas && ($itemDropdown.hasClass('focus') || $itemDropdown.hasClass('show'))) {
      $itemDropdown.removeClass('focus show');
      $dropdownMenu.removeClass('focus show');
    }
  });

  // don't close the menu with the form
  const focusForm = `
    .dropdown-menu:not(.show) input,
    .dropdown-menu:not(.show) textarea,
    .dropdown-menu:not(.show) button,
    .dropdown-menu:not(.show) select
  `;

  $doc.on('focus', focusForm, function () {
    // eslint-disable-next-line newline-per-chained-call
    $(this).parents('.flq-dropdown').addClass('show').children('.dropdown-menu').addClass('show');
  });

  // closing the menu when hover to the other nav-link
  $doc.on('mouseenter', '.flq-dropdown > a', function () {
    const $dropdowns = $(this).closest('.flq-dropdown.focus');

    if ($dropdowns.length) {
      $dropdowns.children('a').blur();
      $dropdowns.removeClass('focus').children('.dropdown-menu').removeClass('focus');
    }
  });

  // show and hide the menu with focus
  function toggleShow() {
    const $thisDropdown = $(this).parents('.flq-dropdown');
    const $thisDropdownMenu = $thisDropdown.children('.dropdown-menu');

    if (!$thisDropdown.hasClass('focus')) {
      $thisDropdown.addClass('focus');
      $thisDropdownMenu.addClass('focus');
    } else {
      $thisDropdown.removeClass('focus');
      $thisDropdownMenu.removeClass('focus');
    }
  }

  $doc.on('focus', '.flq-dropdown a', toggleShow);
  $doc.on('blur', '.flq-dropdown a', toggleShow);

  // update position
  debounceResize(() => {
    $dropdownMenu.each(function () {
      const $thisDropdown = $(this);
      const rect = $thisDropdown[0].getBoundingClientRect();
      const rectLeft = rect.left;
      const rectRight = rect.right;
      const rectWidth = rect.width;
      const wndW = $wnd.width();

      if (wndW - rectRight < 0 && $dropdownMenu.parents('.flq-dropdown-align-left')) {
        $thisDropdown.addClass('flq-dropdown-drop-left');

        if (wndW - rectRight === rectWidth + 10) {
          $thisDropdown.removeClass('flq-dropdown-drop-left');
        }
      }

      if (
        rectLeft < 0 &&
        $dropdownMenu.parents('.flq-dropdown-align-center, .flq-dropdown-align-right')
      ) {
        $thisDropdown.addClass('flq-dropdown-drop-right');

        if (rectLeft === rectWidth + 10) {
          $thisDropdown.removeClass('flq-dropdown-drop-right');
        }
      }
    });
  });

  // Hide when a key is pressed Esc
  $doc.on('keyup', (e) => {
    if (e.keyCode === 27) {
      // hide dropdown
      if ($itemDropdown.hasClass('focus show')) {
        $itemDropdown
          .removeClass('focus show')
          .children('.dropdown-menu')
          .removeClass('focus show');
      }
    }
  });
}

export { initDropdown };
