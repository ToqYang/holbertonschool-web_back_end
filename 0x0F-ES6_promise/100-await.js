// Await and async
import { uploadPhoto, createUser } from './utils';

const asyncUploadUser = async () => {
  let upload;
  let make;

  try {
    upload = await uploadPhoto();
    make = await createUser();
  } catch (e) {
    upload = null;
    make = null;
  }
  return ({ upload, make });
};

export default asyncUploadUser;
