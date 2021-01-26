import api from './api';

export const predictSpecies = async filename => {
  const res = await api.get(`/predict/${filename}`);
  return res.data;
};
