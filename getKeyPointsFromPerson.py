def getKeyPoints(person):
    rightHipPoint, leftHipPoint, rightShoulderPoint, leftShoulderPoint = [0,0]
    
    if (person.hasLeftHip() and person.hasRightHip() and person.hasLeftShoulder\
        and person.hasRightShoulder()):
        rightHipPoint = person.getRightHip()
        leftHipPoint = person.getLeftHip()
        rightShoulderPoint = person.getRightShoulder()
        leftShoulderPoint = person.getLeftShoulder()
    elif ((person.hasLeftEye or person.hasRightEye) and (person.hasRightShoulder()\
        or person.hasLeftShoulder())) or (person.hasRightShoulder() and \
        person.hasLeftShoulder()):
        if person.hasRightShoulder():
            rightShoulderPoint = person.getRightShoulder()
        else:
            if person.getLeftShoulder()[0] < 640/2:
                rightShoulderPoint = [1, person.getLeftShoulder()[1]]
            else:
                distanceToEye = person.getLeftShoulder()[0] - person.getLeftEye()[0]
                rightShoulderPoint = [person.getLeftShoulder()[0] - 2 * distanceToEye,\
                                      person.getLeftShoulder()[1]]
        if person.hasLeftShoulder():
            leftShoulderPoint = person.getLeftShoulder()
        else:
            if person.getRightShoulder()[0] > 640/2:
                leftShoulderPoint = [1, person.getRightShoulder()[1]]
            else:
                distanceToEye = person.getRightShoulder()[0] - person.getRightEye()[0]
                leftShoulderPoint = [person.getRightShoulder()[0] - 2 * distanceToEye,\
                                      person.getRightShoulder()[1]]
        if person.hasRightHip():
            rightHipPoint = person.getRightHip
        else:
            rightHipPoint = [person.getRightShoulder()[0], 479]
        
        if person.hasLeftHip():
            leftHipPoint = person.getLeftHip
        else:
            leftHipPoint = [person.getLeftShoulder()[0], 479]
    else:
        rightHipPoint = [0,479]
        rightShoulderPoint = [0, 0]
        leftShoulderPoint = [639,479]
        leftHipPoint = [639,0]
        
    return [rightHipPoint, rightShoulderPoint, leftShoulderPoint, leftHipPoint]