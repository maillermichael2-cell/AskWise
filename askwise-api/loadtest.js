import http from 'k6/http';
import { sleep } from 'k6';

// 1. Define your load settings
export const options = {
  vus: 10,           // 10 virtual users hitting your API at the exact same time
  duration: '30s',   // Keep the test running for 30 seconds
};

// 2. Define what each virtual user actually does
export default function () {
  // Replace this URL with the working API endpoint you verified in Insomnia
  http.get('localhost/api/v1/documents/upload/'); 
  
  sleep(1);          // Wait 1 second before this user sends another request
}
