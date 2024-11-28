import { options } from './parts/_options';

if (typeof window.Fliqs !== 'undefined') {
  window.Fliqs.setOptions(options);
  window.Fliqs.init();
}
