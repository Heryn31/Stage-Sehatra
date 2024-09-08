const $ = window.jQuery;
const $doc = $(document);

const perfData = window.performance.timing; // The PerformanceTiming interface represents timing-related performance information for the given page.
const EstimatedTime = -(perfData.loadEventEnd - perfData.navigationStart);
const time = Math.max(600, Math.min(600, parseInt((EstimatedTime / 1000) % 60, 10) * 100));

// Preloader Animation
$doc.on('DOMContentLoaded', () => {
  const $preloader = $('.flq-preloader');
  const $preloaderBg = $('.flq-preloader-bg');

  // No preloader available.
  if (!$preloader.length) {
    $doc.trigger('flq.preloader.hide');
    return;
  }

  $preloader.addClass('flq-preloader-show');

  let preloaderTimer;
  function closePreloader() {
    clearTimeout(preloaderTimer);
    $preloader.addClass('flq-preloader-hide').removeClass('flq-preloader-show');
    $preloaderBg.addClass('flq-preloader-bg-hide');
    $doc.trigger('flq.preloader.hide');
  }

  if ($preloader.length) {
    preloaderTimer = setTimeout(closePreloader, time);
  }
});
