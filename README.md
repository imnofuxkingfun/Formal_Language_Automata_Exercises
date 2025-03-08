# DFA Engine and NFA to DFA Converter  

## Project Overview  
This project includes two key components: a **Deterministic Finite Automaton (DFA) engine** and a **converter from a Non-Deterministic Finite Automaton (NFA) to DFA**. The DFA engine simulates the behavior of a DFA by processing input strings and determining their acceptance based on a defined transition system. The NFA to DFA converter takes an NFA as input and constructs an equivalent DFA using the subset construction method.  

## Features  
- DFA Engine:  
  - Defines a DFA with states, an alphabet, transition functions, an initial state, and accepting states.  
  - Processes input strings and determines whether they are accepted or rejected.  

- NFA to DFA Converter:  
  - Converts an NFA into an equivalent DFA using the subset construction algorithm.  
  - Supports epsilon transitions in the NFA.  
  - Outputs the equivalent DFA representation.  

## Usage  
1. Define the states, alphabet, transitions, initial state, and accepting states for the DFA or NFA.  
2. Use the DFA engine to process input strings and determine acceptance.  
3. Use the NFA to DFA converter to transform an NFA into an equivalent DFA.  
4. Run the DFA engine on the converted DFA to verify correctness.  

## Implementation  
- Implemented using data structures such as sets, maps, and queues for efficient state processing.  
- Uses breadth-first search (BFS) for subset construction in NFA to DFA conversion.  
- Handles various types of NFAs, including those with multiple transitions and epsilon moves.  

This project provides a foundational implementation of automata theory concepts, suitable for educational and practical applications.
