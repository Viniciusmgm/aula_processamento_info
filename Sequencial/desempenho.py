vp = int(input())
fn = int(input())
fp = int(input())
vn = int(input())
acur = (vp + vn) / (vp + vn + fp + fn)
prec = vp / (vp + fp)
sens = vp / (vp + fn)
print(round(acur,2))
print(round(prec,2))
print(round(sens,2))