function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%

h_theta = X * theta;
J_nonReg = sum((y-h_theta) .* (y-h_theta)) ./ (2 * rows(y));
J = J_nonReg + (lambda/(2*m)) * theta(2:end)' * theta(2:end);

%size(X')
%size((h_theta - y))
grad_nonReg = (X' * (h_theta - y)) ./ rows(y);
grad_Reg = (lambda / m) * theta;
grad_Reg(1) = 0;
grad = grad_nonReg + grad_Reg;

% =========================================================================

grad = grad(:);

end
