import http from 'k6/http';
import { sleep, check } from 'k6';

export default function () {
  const res = http.get('https://quickpizza.grafana.com/');

  check(res, {
    'Статус 200': (r) => r.status === 200,
    'Ответ меньше 500мс': (r) => r.timings.duration < 500,
  });

  sleep(1);
}
