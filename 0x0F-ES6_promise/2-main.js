import handleResponseFromAPI from "./2-then";

const promise = Promise.reject();
handleResponseFromAPI(promise);
