// Await and async
import { uploadPhoto, createUser } from './utils';

const asyncUploadUser = async () => {
  const upload = await uploadPhoto();
  const make = await createUser();

  return ({ upload, make });
};

export default asyncUploadUser;
