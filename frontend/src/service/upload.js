import api from './api';

export const getTest = async () => {
  const res = await api.get('/files');
  console.log(res.data);
  return res.data;
};

export const uploadTest = async file => {
  let formData = new FormData();
  formData.append('file', file);
  const res = await api.post('/bpi/currentprice.json', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
      'Access-Control-Allow-Origin': '*',
    },
  });
  return res.data;
};
