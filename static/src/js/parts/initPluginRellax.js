import { $, $doc, isMobile } from './_utility';

function initPluginRellax() {
  if (typeof Rellax === 'undefined' || !$('[data-rellax]').length || isMobile) {
    return;
  }

  const rellax = new window.Rellax('[data-rellax]', {
    center: true,
  });

  $doc.imagesLoaded().done(() => {
    rellax.refresh();
  });
}

export { initPluginRellax };
