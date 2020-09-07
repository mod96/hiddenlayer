namespace ADDER
{
	open Microsoft.Quantum.Arithmetic;
	
	operation TestAddition(xValue : Int, yValue : Int, n : Int) : Unit {
	    using ((xQubits, yQubits) = (Qubit[n], Qubit[n]))
	    {
	        let x = LittleEndian(xQubits); // define bit order
	        let y = LittleEndian(yQubits);
        
	        ApplyXorInPlace(xValue, x); // initialize values
	        ApplyXorInPlace(yValue, y);
        
	        AddI(x, y); // perform addition x+y into y
        
	        return y;
	    }
	}
}