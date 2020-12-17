/* Resolve Promise
    This not found a error
    because independent this pass a promise
*/
function handleResponseFromAPI(promise) {
    return promise
        .then(() => {
            return {
                status: 200,
                body: 'Success',
            }
        })
        .catch(() => new Error())
        .finally(() => console.log('Got a response from the API'));
}

export default handleResponseFromAPI;
