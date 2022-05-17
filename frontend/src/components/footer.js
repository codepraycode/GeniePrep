import React from 'react'

function Footer(props) {
    return (
        <footer className={`${props.className} container`}>
            <div className="copyright">
                <span>copyright &copy; 2022</span>
                <span>codepraycode</span>
            </div>
        </footer>
    )
}

export default Footer
