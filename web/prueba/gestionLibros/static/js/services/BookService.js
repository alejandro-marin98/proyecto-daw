export default class BookService {
    async getAllBooks() {
        const url = 'http://localhost:8000/libros/getBooks';

        const response = await fetch(url);
        const data = await response.json();

        return data.libros;
    }
}