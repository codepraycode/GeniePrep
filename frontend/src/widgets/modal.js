import React from 'react';

const Modal = ({title,children, okText, cancelText}) => {
    return (
        <div 
            className="modal fade" 
            id="staticBackdrop" 
            data-bs-backdrop="static" 
            data-bs-keyboard="false" 
            tabindex="-1" 
            aria-labelledby="staticBackdropLabel" 
            aria-hidden="true"
        >
            <div className="modal-dialog">
                <div className="modal-content">
                    <div className="modal-header">
                        <h5 
                            className="modal-title" 
                            id="staticBackdropLabel"
                        >
                            {title}
                        </h5>
                        
                        <button 
                            type="button" 
                            className="btn-close" 
                            data-bs-dismiss="modal" 
                            aria-label="Close"/>
                    </div>

                    <div className="modal-body">
                        {children}
                    </div>

                    <div className="modal-footer">
                        <button 
                            type="button" 
                            class="btn" 
                            data-bs-dismiss="modal"
                        >
                            {cancelText || 'Close'}
                        </button>

                        <button 
                            type="button" 
                            class="btn active"
                        >
                            {okText || "Ok" }
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Modal;