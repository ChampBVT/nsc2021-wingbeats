import api from './api';

export const deleteFile = filename => {
  return api.delete(`/file/${filename}`);
};
