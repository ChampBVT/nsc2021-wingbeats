import api from './api';

export const getFiles = async () => {
  const res = await api.get('/files');
  return res.data;
};

export const getFileHref = filename => {
  return api.defaults.baseURL + `/file/${filename}`;
};
