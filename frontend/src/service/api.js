import axios from 'axios';

const api = axios.create({ baseURL: 'http://localhost/api/v1' });

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
