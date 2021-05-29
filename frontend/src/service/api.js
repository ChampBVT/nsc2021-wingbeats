import axios from 'axios';
import { DEV_BACKEND_URL } from "../constant/service";

const api = axios.create({ baseURL: DEV_BACKEND_URL });

api.interceptors.request.use(
  config => {
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

api.interceptors.response.use(
  response => {
    return response;
  },
  error => {
    if (error.response && error.response.data) return error.response;
    return Promise.reject(error);
  }
);

export default api;
