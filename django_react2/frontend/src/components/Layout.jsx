import { Link, Outlet } from 'react-router-dom'

const Layout = () => {
    return (
        <>
        <header>
            <h1>Книга рецептов</h1>
            <Link to="/">Главная</Link>
            <Link to="category">первое блюдо</Link>
            <Link to="category">основное блюдо</Link>
            <Link to="category">десерт</Link>
        </header>

        <Outlet />
        </>
    )
}

export default Layout