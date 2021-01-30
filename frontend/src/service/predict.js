import api from './api';

export const predictSpecies = async (filename, cancelToken) => {
  const res = await api.get(`/predict/${filename}`, {
    cancelToken: cancelToken.token,
  });
  return res.data;
};
