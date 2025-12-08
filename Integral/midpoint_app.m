% midpoint method application

function midpoint_app()
	v = @(t) 3*(t^2)*exp(t^3);
	n = input("n:");
	numerical = midpoint(v,0,1,n);

	% Compare with exact value
	V = @(t) exp(t^3); % dV/dt = v;
	exact = V(1) - V(0); % exact value of the integral
	fprintf("exact result: %.16f\n",exact);
	fprintf("numerical: %.16f\n",numerical);
	error = exact - numerical;
	fprintf("error (exact-numerical): %g\n",error);
end