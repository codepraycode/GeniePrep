import React from 'react'

function Header({children, className}) {
    return (
        <header className={`${className || ''} container`}>
            {children}
        </header>
    )
}

export default Header;
