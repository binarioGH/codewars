#-*-coding: utf-8-*-
def variableOrNumber(variables, value):
	try:
		value = int(value);
	except:
		value = variables[value];
	return value;

def simple_assembler(program):
	print(program);
	variables = {};
	cmdIndex = 0;
	while cmdIndex <= len(program)-1:
		cmd = program[cmdIndex];
		cmd = cmd.split(" ");
		if(len(cmd) >= 3):
			cmd[2] = variableOrNumber(variables, cmd[2]);
		if(cmd[0] == "mov"):
			variables[cmd[1]] = cmd[2];
		elif(cmd[0] == "inc"):
			variables[cmd[1]] += 1;
		elif(cmd[0] == "dec"):
			variables[cmd[1]] -= 1;
		elif(cmd[0] == "jnz"):
			if(cmd[1] not in variables):
				cmdIndex +=1;
				continue
			if(variables[cmd[1]] != 0):
				cmdIndex += cmd[2];
				continue;
		cmdIndex +=1;
	print(variables)
	return variables;
