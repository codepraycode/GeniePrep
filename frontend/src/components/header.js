import React from 'react'

function Header(props) {
    return (
        <header className='container'>
            {props.children}
        </header>
    )
}

export default Header;
