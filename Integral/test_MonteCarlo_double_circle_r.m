function test_MonteCarlo_double_circle_r()
    pkg load symbolic; % needed to use sym
    
    % Check the integral of r over a circle with radius 2.
    function result = g(x,y)
        xc = 0; yc = 0;
        R = 2;
        result = R^2 - ((x-xc)^2 + (y-yc)^2);
    end
    g_handle = @g;
    
    % Exact: integral of r*r*dr over circle with radius R becomes
    % 2*pi*1/3*R**3
    syms r;
    I_exact = double(int(2*sym('pi')*r^2, r, 0, 2));
    fprintf('Exact integral: %g\n', I_exact);
    x0 = -2;  x1 = 2;  y0 = -2;  y1 = 2;
    n = 1000;
    rand("seed", 6);                
    I_expected = 16.85949525320151 
    I_computed = MonteCarlo_double(...
               @(x, y) sqrt(x^2 + y^2), g_handle, x0, x1, y0, y1, n);
    fprintf('MC approximation (%d samples): %.16f\n', n^2, I_computed);
    assert(abs(I_computed - I_expected) < 1E-15);
end
