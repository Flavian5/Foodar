import axios from 'axios';
const defaultOptions = {
    baseURL: 'http://localhost:5000/',
    timeout: 20000
}
const apiClient = axios.create(defaultOptions);

export default apiClient;