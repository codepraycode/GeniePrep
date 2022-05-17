import React from 'react'

function Form ({classes, submitTo, inputHandler, error_info,children}) {
    return (
        <form 
            onSubmit={submitTo} 
            className={`${classes || ''}`} 
        >
            {/* Error Display */}
            <span className="error_info">{error_info}</span>

            {/* Form Content */}
            {            
                children
            }
            

        </form>
    )
}


function FormContent (props) {
    const {inputHandler, children} = props;
    
    return (
        <>
            {/* Form Content */}
            {
                !Array.isArray(children) ?
                <>
                    {
                        <children.type key={children.key || -9999} {...children.props} inputHandler={inputHandler}>
                            {children.props.children}
                        </children.type>
                    }
                </>
                :
                children.map((child, index) => {

                    return (
                        <child.type key={child.key || index} {...child.props} inputHandler={inputHandler}>
                            {child.props.children}
                        </child.type>
                    )
                })
            }
            

        </>
    )
}
// export default Form
export {Form, FormContent}
