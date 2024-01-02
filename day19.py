import constants

data = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:A,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{x<39:R,x<40:three,x<41:A,R}
two{x<4000:R,m<4000:three,A}
three{s>2:R,s>3999:A,R}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3335:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""
data = constants.day19_2


#data = constants.day19
data_lines = data.split("\n")

def invert(obj, pool = None):
    if pool == None:
        pool = default
    tmp = obj.copy()
    for char_loop in obj:
        tmp[char_loop] = pool[char_loop].difference(tmp[char_loop])
    return tmp

default = {char: set(range(1,4001)) for char in "xmas"}
none = {char: set() for char in "xmas"}
def find_all_ranges_that_accept_and_reject(workflow: str, accepts: dict[str, set] = none, rejects: dict = none, pool: dict[str, set] = default):
    pool = pool.copy()
    
    if workflow == "A":
        return pool.copy(), none.copy()
    if workflow == "R":
        return none.copy(), pool.copy()
    
    accepts = accepts.copy()
    rejects = rejects.copy()

    rules = workflows[workflow]

    for path in rules[:-1]:
        rule = path.split(":")[0]
        char = rule[0]
        t_range = pool[char].intersection(to_range(rule[1:]))
        if path.split(":")[1] == "A":
            accepts[char] = pool[char].intersection(t_range.difference(rejects[char]).union(accepts[char]))
        elif path.split(":")[1] == "R":
            rejects[char] = pool[char].intersection(t_range.difference(accepts[char]).union(rejects[char]))
        else:
            if len(t_range.difference(accepts[char]).difference(rejects[char])) > 0:
                new_pool = pool.copy()
                new_pool[char] = new_pool[char].intersection(t_range.difference(accepts[char]).difference(rejects[char]))
                acceptions, rejections = find_all_ranges_that_accept_and_reject(path.split(":")[1],accepts,rejects,new_pool)
                can_pass = False
                for o_char in "xmas":
                    if len(acceptions[o_char].difference(accepts[o_char]).difference(rejects[o_char])) > 0:
                        accepts[char] = accepts[char].union(t_range.difference(accepts[char]).difference(rejects[char]))
                        accepts[o_char] = accepts[o_char].union(acceptions[o_char].difference(accepts[o_char]).difference(rejects[o_char]))
                        can_pass = True
                
                if can_pass:
                    pass
                else:
                    accepts[char] = default[char].intersection(acceptions[char].difference(rejects[char]).union(accepts[char]))
                    rejects[char] = pool[char].intersection(rejections[char].difference(accepts[char]).union(rejects[char]))

    # is having
    if rules[-1] == "A":
        return invert(rejects, pool), rejects
    elif rules[-1] == "R":
        return accepts, invert(accepts, pool)
    else:
        return find_all_ranges_that_accept_and_reject(rules[-1], accepts, rejects, pool)
        
workflows = {}
objects = []

def parse_workflow(string, object):
    if string == "A": return 1
    if string == "R": return 0

    workflow = workflows[string]

    for rule in workflow:
        if ":" in rule:
            expression = rule.split(":")[0]
            new_rule = rule.split(":")[1]
            if (">" in expression) and (expression[0] in object) and (object[expression[0]] > int(expression.split(">")[1])):
                return parse_workflow(new_rule, object)
            if ("<" in expression) and (expression[0] in object) and (object[expression[0]] < int(expression.split("<")[1])):
                return parse_workflow(new_rule, object)
        else:
            return parse_workflow(rule, object)

def find_all_workflows_that_point_to_workflow(to_workflow: str) -> list:
    ret = []
    for workflow in workflows:
        if not ":" in workflows[workflow][-1] and workflows[workflow][-1] == to_workflow:
            ret.append(workflow)
            continue
        for rule in workflows[workflow]:
            if ":" in rule and rule.split(":")[1] == to_workflow:
                ret.append(workflow)
                break
    return ret

def to_range(repr, reverse = False):
    if (repr[0] == ">" and not reverse) or (repr[0] == "<" and reverse):
        return set(range(int(repr[1:])+1, 4001))
    elif (repr[0] == "<" and not reverse) or (repr[0] == ">" and reverse):
        return set(range(1,int(repr[1:])))

def main():

    workflows_string = data.split("\n\n")[0]
    inputs_string = data.split("\n\n")[1]

    for workflow_line in workflows_string.split("\n"):
        workflows[workflow_line.split("{")[0]] = workflow_line.split("{")[1][:-1].split(",")
    
    for input_line in inputs_string.split("\n"):
        input_line = input_line[1:-1]
        obj = {}
        for declaration in input_line.split(","):
            obj[declaration.split("=")[0]] = int(declaration.split("=")[1])
        objects.append(obj)

    summed = 0
    for object in objects:
        summed += parse_workflow( "in",object ) * (object["x"] + object["m"] + object["a"] + object["s"])
        
    accepts = find_all_ranges_that_accept_and_reject("in")[0]
    combinations = 1
    print(accepts)
    for char_loop in "xmas":
        if len(accepts[char_loop]) > 0:
            combinations *= len(accepts[char_loop])
    print(summed, combinations)

    x,m,a,s = "x","m","a","s"
    for obj in [
        {x:787,m:2655,a:1222,s:2876},
        {x:1679,m:44,a:2067,s:496},
        {x:2036,m:264,a:79,s:2244},
        {x:2461,m:1339,a:466,s:291},
        {x:2127,m:1623,a:2188,s:1013}
    ]:
        accept = False
        for char in obj:
            if obj[char] in accepts[char]:
                accept = True
        print(accept)

167409079868000
165120000000000

main()


