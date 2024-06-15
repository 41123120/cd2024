# NX 1872
# Journal created by Administrator on Fri Jun 14 21:39:36 2024 台北標準時間

#
import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Assemblies
import NXOpen.Drawings
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    # ----------------------------------------------
    #   功能表：檔案(F)->新建(N)...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    fileNew1 = theSession.Parts.FileNew()
    
    theSession.SetUndoMarkName(markId1, "新建 對話方塊")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "新建")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "新建")
    
    fileNew1.TemplateFileName = "model-plain-1-mm-template.prt"
    
    fileNew1.UseBlankTemplate = False
    
    fileNew1.ApplicationName = "ModelTemplate"
    
    fileNew1.Units = NXOpen.Part.Units.Millimeters
    
    fileNew1.RelationType = ""
    
    fileNew1.UsesMasterModel = "No"
    
    fileNew1.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew1.TemplatePresentationName = "模型"
    
    fileNew1.ItemType = ""
    
    fileNew1.Specialization = ""
    
    fileNew1.SetCanCreateAltrep(False)
    
    fileNew1.NewFileName = "E:\\tuan\\model1.prt"
    
    fileNew1.MasterFileName = ""
    
    fileNew1.MakeDisplayedPart = True
    
    fileNew1.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    nXObject1 = fileNew1.Commit()
    
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    theSession.DeleteUndoMark(markId3, None)
    
    fileNew1.Destroy()
    
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖(H)...
    # ----------------------------------------------
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder1.PlaneReference = plane1
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder1 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder1.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId4, "建立草圖 對話方塊")
    
    datumAxis1 = workPart.Datums.FindObject("DATUM_CSYS(0) X axis")
    direction1 = workPart.Directions.CreateDirection(datumAxis1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumPlane1 = workPart.Datums.FindObject("DATUM_CSYS(0) XZ plane")
    datumCsys1 = workPart.Features.FindObject("DATUM_CSYS(0)")
    point1 = datumCsys1.FindObject("POINT 1")
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(datumPlane1, direction1, point1, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, True)
    
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder1.Csystem = cartesianCoordinateSystem1
    
    origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal2 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane2 = workPart.Planes.CreatePlane(origin2, normal2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane2.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom1 = [NXOpen.NXObject.Null] * 1 
    geom1[0] = datumPlane1
    plane2.SetGeometry(geom1)
    
    plane2.SetFlip(True)
    
    plane2.SetExpression(None)
    
    plane2.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane2.Evaluate()
    
    origin3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal3 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane3 = workPart.Planes.CreatePlane(origin3, normal3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane3.SynchronizeToPlane(plane2)
    
    plane3.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom2 = [NXOpen.NXObject.Null] * 1 
    geom2[0] = datumPlane1
    plane3.SetGeometry(geom2)
    
    plane3.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane3.Evaluate()
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.DeleteUndoMark(markId5, None)
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject2 = sketchInPlaceBuilder1.Commit()
    
    sketch1 = nXObject2
    feature1 = sketch1.Feature
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId7)
    
    sketch1.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId6, None)
    
    theSession.SetUndoMarkName(markId4, "建立草圖")
    
    sketchInPlaceBuilder1.Destroy()
    
    sketchAlongPathBuilder1.Destroy()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression2)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression1)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane1.DestroyPlane()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression4)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression3)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane3.DestroyPlane()
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->矩形(R)...
    # ----------------------------------------------
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    theSession.SetUndoMarkVisibility(markId9, "Create Rectangle", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    # Creating rectangle using From Center method 
    # ----------------------------------------------
    startPoint1 = NXOpen.Point3d(-38.421022336033481, 0.0, -42.000000000000057)
    endPoint1 = NXOpen.Point3d(-38.421022336033438, 0.0, 41.999999999999943)
    line1 = workPart.Curves.CreateLine(startPoint1, endPoint1)
    
    startPoint2 = NXOpen.Point3d(-38.421022336033438, 0.0, 41.999999999999943)
    endPoint2 = NXOpen.Point3d(38.421022336033538, 0.0, 42.0)
    line2 = workPart.Curves.CreateLine(startPoint2, endPoint2)
    
    startPoint3 = NXOpen.Point3d(38.421022336033538, 0.0, 42.0)
    endPoint3 = NXOpen.Point3d(38.421022336033495, 0.0, -42.0)
    line3 = workPart.Curves.CreateLine(startPoint3, endPoint3)
    
    startPoint4 = NXOpen.Point3d(38.421022336033495, 0.0, -42.0)
    endPoint4 = NXOpen.Point3d(-38.421022336033481, 0.0, -42.000000000000057)
    line4 = workPart.Curves.CreateLine(startPoint4, endPoint4)
    
    theSession.ActiveSketch.AddGeometry(line1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line3, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line4, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_1.Geometry = line1
    geom1_1.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_1.SplineDefiningPointIndex = 0
    geom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_1.Geometry = line2
    geom2_1.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint1 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_1, geom2_1)
    
    geom1_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_2.Geometry = line2
    geom1_2.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_2.SplineDefiningPointIndex = 0
    geom2_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_2.Geometry = line3
    geom2_2.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_2.SplineDefiningPointIndex = 0
    sketchGeometricConstraint2 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_2, geom2_2)
    
    geom1_3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_3.Geometry = line3
    geom1_3.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_3.SplineDefiningPointIndex = 0
    geom2_3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_3.Geometry = line4
    geom2_3.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint3 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_3, geom2_3)
    
    geom1_4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_4.Geometry = line4
    geom1_4.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_4.SplineDefiningPointIndex = 0
    geom2_4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_4.Geometry = line1
    geom2_4.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint4 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_4, geom2_4)
    
    geom3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom3.Geometry = line2
    geom3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint5 = theSession.ActiveSketch.CreateHorizontalConstraint(geom3)
    
    conGeom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_1.Geometry = line1
    conGeom1_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_1.SplineDefiningPointIndex = 0
    conGeom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_1.Geometry = line2
    conGeom2_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint6 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_1, conGeom2_1)
    
    conGeom1_2 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_2.Geometry = line2
    conGeom1_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_2.SplineDefiningPointIndex = 0
    conGeom2_2 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_2.Geometry = line3
    conGeom2_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_2.SplineDefiningPointIndex = 0
    sketchGeometricConstraint7 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_2, conGeom2_2)
    
    conGeom1_3 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_3.Geometry = line3
    conGeom1_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_3.SplineDefiningPointIndex = 0
    conGeom2_3 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_3.Geometry = line4
    conGeom2_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint8 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_3, conGeom2_3)
    
    conGeom1_4 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_4.Geometry = line4
    conGeom1_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_4.SplineDefiningPointIndex = 0
    conGeom2_4 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_4.Geometry = line1
    conGeom2_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint9 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_4, conGeom2_4)
    
    conGeom1_5 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys2 = workPart.Features.FindObject("SKETCH(1:1B)")
    point2 = datumCsys2.FindObject("POINT 1")
    conGeom1_5.Geometry = point2
    conGeom1_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_5.SplineDefiningPointIndex = 0
    conGeom2_5 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_5.Geometry = line1
    conGeom2_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_5.SplineDefiningPointIndex = 0
    sketchGeometricConstraint10 = theSession.ActiveSketch.CreateMidpointConstraint(conGeom1_5, conGeom2_5)
    
    conGeom1_6 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_6.Geometry = point2
    conGeom1_6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_6.SplineDefiningPointIndex = 0
    conGeom2_6 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_6.Geometry = line2
    conGeom2_6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint11 = theSession.ActiveSketch.CreateMidpointConstraint(conGeom1_6, conGeom2_6)
    
    dimObject1_1 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_1.Geometry = line1
    dimObject1_1.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_1.AssocValue = 0
    dimObject1_1.HelpPoint.X = 0.0
    dimObject1_1.HelpPoint.Y = 0.0
    dimObject1_1.HelpPoint.Z = 0.0
    dimObject1_1.View = NXOpen.NXObject.Null
    dimObject2_1 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_1.Geometry = line1
    dimObject2_1.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_1.AssocValue = 0
    dimObject2_1.HelpPoint.X = 0.0
    dimObject2_1.HelpPoint.Y = 0.0
    dimObject2_1.HelpPoint.Z = 0.0
    dimObject2_1.View = NXOpen.NXObject.Null
    dimOrigin1 = NXOpen.Point3d(-27.923674425230253, 0.0, -6.2171143362784929e-14)
    sketchDimensionalConstraint1 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_1, dimObject2_1, dimOrigin1, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint1 = sketchDimensionalConstraint1
    dimension1 = sketchHelpedDimensionalConstraint1.AssociatedDimension
    
    expression5 = sketchHelpedDimensionalConstraint1.AssociatedExpression
    
    dimObject1_2 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_2.Geometry = line2
    dimObject1_2.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_2.AssocValue = 0
    dimObject1_2.HelpPoint.X = 0.0
    dimObject1_2.HelpPoint.Y = 0.0
    dimObject1_2.HelpPoint.Z = 0.0
    dimObject1_2.View = NXOpen.NXObject.Null
    dimObject2_2 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_2.Geometry = line2
    dimObject2_2.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_2.AssocValue = 0
    dimObject2_2.HelpPoint.X = 0.0
    dimObject2_2.HelpPoint.Y = 0.0
    dimObject2_2.HelpPoint.Z = 0.0
    dimObject2_2.View = NXOpen.NXObject.Null
    dimOrigin2 = NXOpen.Point3d(5.7503338544243317e-14, 0.0, 31.502652089196765)
    sketchDimensionalConstraint2 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_2, dimObject2_2, dimOrigin2, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint2 = sketchDimensionalConstraint2
    dimension2 = sketchHelpedDimensionalConstraint2.AssociatedDimension
    
    expression6 = sketchHelpedDimensionalConstraint2.AssociatedExpression
    
    dimObject1_3 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_3.Geometry = line1
    dimObject1_3.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_3.AssocValue = 0
    dimObject1_3.HelpPoint.X = -38.421022336033481
    dimObject1_3.HelpPoint.Y = 0.0
    dimObject1_3.HelpPoint.Z = -42.000000000000057
    dimObject1_3.View = NXOpen.NXObject.Null
    dimObject2_3 = NXOpen.Sketch.DimensionGeometry()
    
    datumAxis2 = workPart.Datums.FindObject("SKETCH(1:1B) X axis")
    dimObject2_3.Geometry = datumAxis2
    dimObject2_3.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_3.AssocValue = 0
    dimObject2_3.HelpPoint.X = 28.574999999999999
    dimObject2_3.HelpPoint.Y = 0.0
    dimObject2_3.HelpPoint.Z = 0.0
    dimObject2_3.View = NXOpen.NXObject.Null
    dimOrigin3 = NXOpen.Point3d(-30.998276443830079, 0.0, -7.4227458922033849)
    sketchDimensionalConstraint3 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.AngularDim, dimObject1_3, dimObject2_3, dimOrigin3, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension3 = sketchDimensionalConstraint3.AssociatedDimension
    
    expression7 = sketchDimensionalConstraint3.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    geoms1 = [NXOpen.SmartObject.Null] * 4 
    geoms1[0] = line1
    geoms1[1] = line2
    geoms1[2] = line3
    geoms1[3] = line4
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms1)
    
    geoms2 = [NXOpen.SmartObject.Null] * 4 
    geoms2[0] = line1
    geoms2[1] = line2
    geoms2[2] = line3
    geoms2[3] = line4
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms2)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖約束(K)->尺寸(D)->快速(P)...
    # ----------------------------------------------
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchRapidDimensionBuilder1 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines1 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBefore(lines1)
    
    lines2 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAfter(lines2)
    
    lines3 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAbove(lines3)
    
    lines4 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBelow(lines4)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder1.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines5 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBefore(lines5)
    
    lines6 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAfter(lines6)
    
    lines7 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAbove(lines7)
    
    lines8 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBelow(lines8)
    
    theSession.SetUndoMarkName(markId10, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder1.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits1 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits2 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits3 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits4 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits5 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits6 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits7 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits8 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits9 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits10 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder1.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder1.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits11 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits12 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits13 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits14 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits15 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits16 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits17 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits18 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits19 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits20 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    point3 = NXOpen.Point3d(11.881199678211203, 0.0, 41.999999999999979)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(line2, workPart.ModelingViews.WorkView, point3)
    
    point1_1 = NXOpen.Point3d(38.421022336033538, 0.0, 42.0)
    point2_1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line2, workPart.ModelingViews.WorkView, point1_1, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_1)
    
    point1_2 = NXOpen.Point3d(-38.421022336033438, 0.0, 41.999999999999943)
    point2_2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line2, workPart.ModelingViews.WorkView, point1_2, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_2)
    
    dimensionlinearunits21 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits22 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits23 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits24 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits25 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits26 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin1 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin1.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin1.View = NXOpen.View.Null
    assocOrigin1.ViewOfGeometry = workPart.ModelingViews.WorkView
    point4 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin1.PointOnGeometry = point4
    assocOrigin1.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.DimensionLine = 0
    assocOrigin1.AssociatedView = NXOpen.View.Null
    assocOrigin1.AssociatedPoint = NXOpen.Point.Null
    assocOrigin1.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.XOffsetFactor = 0.0
    assocOrigin1.YOffsetFactor = 0.0
    assocOrigin1.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder1.Origin.SetAssociativeOrigin(assocOrigin1)
    
    point5 = NXOpen.Point3d(15.89303333578899, 0.0, 66.966761822644784)
    sketchRapidDimensionBuilder1.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point5)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder1.Style.DimensionStyle.TextCentered = False
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject3 = sketchRapidDimensionBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId11, None)
    
    theSession.SetUndoMarkName(markId10, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId10, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder1.Destroy()
    
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder2 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines9 = []
    sketchRapidDimensionBuilder2.AppendedText.SetBefore(lines9)
    
    lines10 = []
    sketchRapidDimensionBuilder2.AppendedText.SetAfter(lines10)
    
    lines11 = []
    sketchRapidDimensionBuilder2.AppendedText.SetAbove(lines11)
    
    lines12 = []
    sketchRapidDimensionBuilder2.AppendedText.SetBelow(lines12)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder2.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId12, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder2.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits27 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits28 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits29 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits30 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits31 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits32 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits33 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits34 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits35 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits36 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder2.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits37 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits38 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits39 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits40 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits41 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits42 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits43 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits44 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits45 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits46 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    expression8 = workPart.Expressions.FindObject("p0")
    expression8.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId12, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.Scale(0.26027417783261375)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId13, None)
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId12, "Edit Driving Value")
    
    scaleAboutPoint1 = NXOpen.Point3d(14.041417801522304, -1.5430129452222308, 0.0)
    viewCenter1 = NXOpen.Point3d(-14.041417801522304, 1.5430129452222308, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(11.233134241217842, -1.2344103561777844, 0.0)
    viewCenter2 = NXOpen.Point3d(-11.233134241217842, 1.2344103561777844, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(8.9865073929742572, -0.98752828494222744, 0.0)
    viewCenter3 = NXOpen.Point3d(-8.9865073929742572, 0.98752828494222744, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(7.1892059143794329, -0.79002262795378209, 0.0)
    viewCenter4 = NXOpen.Point3d(-7.1892059143794196, 0.79002262795378209, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(5.7513647315035232, -0.37921086141781735, 0.0)
    viewCenter5 = NXOpen.Point3d(-5.7513647315035232, 0.37921086141781735, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint5, viewCenter5)
    
    scaleAboutPoint6 = NXOpen.Point3d(4.4999688888247311, -0.20224579275616647, 0.0)
    viewCenter6 = NXOpen.Point3d(-4.4999688888247311, 0.20224579275616647, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(3.2763818426499247, 0.40449158551233622, 0.0)
    viewCenter7 = NXOpen.Point3d(-3.2763818426499114, -0.40449158551233622, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint7, viewCenter7)
    
    point6 = NXOpen.Point3d(9.9999999999996128, 0.0, 1.9012329054153074)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(line3, workPart.ModelingViews.WorkView, point6)
    
    point1_3 = NXOpen.Point3d(9.9999999999996181, 0.0, 10.931515468969778)
    point2_3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line3, workPart.ModelingViews.WorkView, point1_3, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_3)
    
    point1_4 = NXOpen.Point3d(9.9999999999996074, 0.0, -10.931515468969778)
    point2_4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line3, workPart.ModelingViews.WorkView, point1_4, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_4)
    
    dimensionlinearunits47 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits48 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits49 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits50 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits51 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits52 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin2 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin2.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin2.View = NXOpen.View.Null
    assocOrigin2.ViewOfGeometry = workPart.ModelingViews.WorkView
    point7 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin2.PointOnGeometry = point7
    assocOrigin2.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.DimensionLine = 0
    assocOrigin2.AssociatedView = NXOpen.View.Null
    assocOrigin2.AssociatedPoint = NXOpen.Point.Null
    assocOrigin2.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.XOffsetFactor = 0.0
    assocOrigin2.YOffsetFactor = 0.0
    assocOrigin2.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder2.Origin.SetAssociativeOrigin(assocOrigin2)
    
    point8 = NXOpen.Point3d(20.800472195433436, 0.0, 0.47742252441188426)
    sketchRapidDimensionBuilder2.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point8)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.TextCentered = True
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject4 = sketchRapidDimensionBuilder2.Commit()
    
    theSession.DeleteUndoMark(markId15, None)
    
    theSession.SetUndoMarkName(markId14, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId14, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder2.Destroy()
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder3 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines13 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBefore(lines13)
    
    lines14 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAfter(lines14)
    
    lines15 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAbove(lines15)
    
    lines16 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBelow(lines16)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder3.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId16, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder3.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits53 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits54 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits55 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits56 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits57 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits58 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits59 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits60 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits61 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits62 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder3.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits63 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits64 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits65 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits66 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits67 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits68 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits69 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits70 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits71 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits72 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    expression9 = workPart.Expressions.FindObject("p1")
    expression9.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId16, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId17, None)
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId16, "Edit Driving Value")
    
    # ----------------------------------------------
    #   功能表：檔案(F)->完成草圖(K)
    # ----------------------------------------------
    sketchRapidDimensionBuilder3.Destroy()
    
    theSession.UndoToMark(markId18, None)
    
    theSession.DeleteUndoMark(markId18, None)
    
    sketchRapidDimensionBuilder3.Destroy()
    
    sketch2 = theSession.ActiveSketch
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   功能表：插入(S)->設計特徵(E)->拉伸(X)...
    # ----------------------------------------------
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder1.Section = section1
    
    extrudeBuilder1.AllowSelfIntersectingSection(True)
    
    unit2 = extrudeBuilder1.Draft.FrontDraftAngle.Units
    
    expression10 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder1.DistanceTolerance = 0.01
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("35.5")
    
    extrudeBuilder1.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId20, "拉伸 對話方塊")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features1 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature1 = feature1
    features1[0] = sketchFeature1
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1)
    
    section1.AllowSelfIntersection(True)
    
    rules1 = [None] * 1 
    rules1[0] = curveFeatureRule1
    helpPoint1 = NXOpen.Point3d(-10.000000000000004, 0.0, -4.1404276964955606)
    section1.AddToSection(rules1, line1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId22, None)
    
    direction2 = workPart.Directions.CreateDirection(sketch2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder1.Direction = direction2
    
    expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId21, None)
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("30")
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId23, None)
    
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder1.ParentFeatureInternal = False
    
    feature2 = extrudeBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId24, None)
    
    theSession.SetUndoMarkName(markId20, "拉伸")
    
    expression12 = extrudeBuilder1.Limits.StartExtend.Value
    expression13 = extrudeBuilder1.Limits.EndExtend.Value
    extrudeBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression10)
    
    workPart.Expressions.Delete(expression11)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖(H)...
    # ----------------------------------------------
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchInPlaceBuilder2 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal4 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane4 = workPart.Planes.CreatePlane(origin4, normal4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder2.PlaneReference = plane4
    
    expression14 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression15 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder2 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder2.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId25, "建立草圖 對話方塊")
    
    scalar1 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrude1 = feature2
    edge1 = extrude1.FindObject("EDGE * 130 * 170 {(10,-30,-10)(0,-30,-10)(-10,-30,-10) EXTRUDE(2)}")
    point9 = workPart.Points.CreatePoint(edge1, scalar1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction3 = workPart.Directions.CreateDirection(edge1, NXOpen.Sense.Reverse, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face1 = extrude1.FindObject("FACE 130 {(0,-30,0) EXTRUDE(2)}")
    xform2 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction3, point9, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem2 = workPart.CoordinateSystems.CreateCoordinateSystem(xform2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder2.Csystem = cartesianCoordinateSystem2
    
    origin5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal5 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane5 = workPart.Planes.CreatePlane(origin5, normal5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane5.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom4 = [NXOpen.NXObject.Null] * 1 
    geom4[0] = face1
    plane5.SetGeometry(geom4)
    
    plane5.SetFlip(False)
    
    plane5.SetExpression(None)
    
    plane5.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane5.Evaluate()
    
    origin6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal6 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane6 = workPart.Planes.CreatePlane(origin6, normal6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression16 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression17 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane6.SynchronizeToPlane(plane5)
    
    scalar2 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point10 = workPart.Points.CreatePoint(edge1, scalar2, NXOpen.PointCollection.PointOnCurveLocationOption.PercentParameter, NXOpen.Point.Null, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane6.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom5 = [NXOpen.NXObject.Null] * 1 
    geom5[0] = face1
    plane6.SetGeometry(geom5)
    
    plane6.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane6.Evaluate()
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.DeleteUndoMark(markId26, None)
    
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject5 = sketchInPlaceBuilder2.Commit()
    
    sketch3 = nXObject5
    feature3 = sketch3.Feature
    
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId28)
    
    sketch3.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId27, None)
    
    theSession.SetUndoMarkName(markId25, "建立草圖")
    
    sketchInPlaceBuilder2.Destroy()
    
    sketchAlongPathBuilder2.Destroy()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression15)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    workPart.Points.DeletePoint(point10)
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression14)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane4.DestroyPlane()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression17)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression16)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane6.DestroyPlane()
    
    scaleAboutPoint8 = NXOpen.Point3d(-3.2403271849666639, 4.0118336575778049, 0.0)
    viewCenter8 = NXOpen.Point3d(3.2403271849666639, -4.0118336575778049, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint8, viewCenter8)
    
    scaleAboutPoint9 = NXOpen.Point3d(-2.8391438192088962, 3.7032310685333534, 0.0)
    viewCenter9 = NXOpen.Point3d(2.8391438192088962, -3.7032310685333534, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint9, viewCenter9)
    
    scaleAboutPoint10 = NXOpen.Point3d(-2.4688207123555688, 2.9625848548266824, 0.0)
    viewCenter10 = NXOpen.Point3d(2.4688207123555688, -2.9625848548266824, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(-3.7131063513827804, 4.58213124213193, 0.0)
    viewCenter11 = NXOpen.Point3d(3.7131063513827804, -4.5821312421319433, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(-2.9704850811062236, 3.7921086141781526, 0.0)
    viewCenter12 = NXOpen.Point3d(2.9704850811062236, -3.7921086141781633, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint12, viewCenter12)
    
    scaleAboutPoint13 = NXOpen.Point3d(-2.5786338576411456, 3.3370555804767634, 0.0)
    viewCenter13 = NXOpen.Point3d(2.5786338576411456, -3.3370555804767803, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint13, viewCenter13)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->矩形(R)...
    # ----------------------------------------------
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    theSession.SetUndoMarkVisibility(markId30, "Create Rectangle", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    # Creating rectangle using By 2 Points method 
    # ----------------------------------------------
    startPoint5 = NXOpen.Point3d(-10.000000000000004, -30.0, -10.0)
    endPoint5 = NXOpen.Point3d(-7.0000000000000036, -30.0, -10.0)
    line5 = workPart.Curves.CreateLine(startPoint5, endPoint5)
    
    startPoint6 = NXOpen.Point3d(-7.0000000000000036, -30.0, -10.0)
    endPoint6 = NXOpen.Point3d(-7.0000000000000036, -30.0, -5.0)
    line6 = workPart.Curves.CreateLine(startPoint6, endPoint6)
    
    startPoint7 = NXOpen.Point3d(-7.0000000000000036, -30.0, -5.0)
    endPoint7 = NXOpen.Point3d(-10.000000000000004, -30.0, -5.0)
    line7 = workPart.Curves.CreateLine(startPoint7, endPoint7)
    
    startPoint8 = NXOpen.Point3d(-10.000000000000004, -30.0, -5.0)
    endPoint8 = NXOpen.Point3d(-10.000000000000004, -30.0, -10.0)
    line8 = workPart.Curves.CreateLine(startPoint8, endPoint8)
    
    theSession.ActiveSketch.AddGeometry(line5, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line6, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line7, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line8, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_5 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_5.Geometry = line5
    geom1_5.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_5.SplineDefiningPointIndex = 0
    geom2_5 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_5.Geometry = line6
    geom2_5.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_5.SplineDefiningPointIndex = 0
    sketchGeometricConstraint12 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_5, geom2_5)
    
    geom1_6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_6.Geometry = line6
    geom1_6.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_6.SplineDefiningPointIndex = 0
    geom2_6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_6.Geometry = line7
    geom2_6.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint13 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_6, geom2_6)
    
    geom1_7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_7.Geometry = line7
    geom1_7.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_7.SplineDefiningPointIndex = 0
    geom2_7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_7.Geometry = line8
    geom2_7.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_7.SplineDefiningPointIndex = 0
    sketchGeometricConstraint14 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_7, geom2_7)
    
    geom1_8 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_8.Geometry = line8
    geom1_8.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_8.SplineDefiningPointIndex = 0
    geom2_8 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_8.Geometry = line5
    geom2_8.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_8.SplineDefiningPointIndex = 0
    sketchGeometricConstraint15 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_8, geom2_8)
    
    geom6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom6.Geometry = line5
    geom6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint16 = theSession.ActiveSketch.CreateHorizontalConstraint(geom6)
    
    conGeom1_7 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_7.Geometry = line5
    conGeom1_7.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_7.SplineDefiningPointIndex = 0
    conGeom2_7 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_7.Geometry = line6
    conGeom2_7.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_7.SplineDefiningPointIndex = 0
    sketchGeometricConstraint17 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_7, conGeom2_7)
    
    conGeom1_8 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_8.Geometry = line6
    conGeom1_8.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_8.SplineDefiningPointIndex = 0
    conGeom2_8 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_8.Geometry = line7
    conGeom2_8.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_8.SplineDefiningPointIndex = 0
    sketchGeometricConstraint18 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_8, conGeom2_8)
    
    conGeom1_9 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_9.Geometry = line7
    conGeom1_9.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_9.SplineDefiningPointIndex = 0
    conGeom2_9 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_9.Geometry = line8
    conGeom2_9.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_9.SplineDefiningPointIndex = 0
    sketchGeometricConstraint19 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_9, conGeom2_9)
    
    conGeom1_10 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_10.Geometry = line8
    conGeom1_10.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_10.SplineDefiningPointIndex = 0
    conGeom2_10 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_10.Geometry = line5
    conGeom2_10.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_10.SplineDefiningPointIndex = 0
    sketchGeometricConstraint20 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_10, conGeom2_10)
    
    geom1_9 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_9.Geometry = line5
    geom1_9.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_9.SplineDefiningPointIndex = 0
    geom2_9 = NXOpen.Sketch.ConstraintGeometry()
    
    edge2 = extrude1.FindObject("EDGE * 130 * 140 {(-10,-30,-10)(-10,-30,0)(-10,-30,10) EXTRUDE(2)}")
    geom2_9.Geometry = edge2
    geom2_9.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_9.SplineDefiningPointIndex = 0
    sketchGeometricConstraint21 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_9, geom2_9)
    
    dimObject1_4 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_4.Geometry = line5
    dimObject1_4.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_4.AssocValue = 0
    dimObject1_4.HelpPoint.X = 0.0
    dimObject1_4.HelpPoint.Y = 0.0
    dimObject1_4.HelpPoint.Z = 0.0
    dimObject1_4.View = NXOpen.NXObject.Null
    dimObject2_4 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_4.Geometry = line5
    dimObject2_4.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_4.AssocValue = 0
    dimObject2_4.HelpPoint.X = 0.0
    dimObject2_4.HelpPoint.Y = 0.0
    dimObject2_4.HelpPoint.Z = 0.0
    dimObject2_4.View = NXOpen.NXObject.Null
    dimOrigin4 = NXOpen.Point3d(-8.5000000000000036, -30.0, -12.751816770729594)
    sketchDimensionalConstraint4 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_4, dimObject2_4, dimOrigin4, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint3 = sketchDimensionalConstraint4
    dimension4 = sketchHelpedDimensionalConstraint3.AssociatedDimension
    
    expression18 = sketchHelpedDimensionalConstraint3.AssociatedExpression
    
    dimObject1_5 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_5.Geometry = line6
    dimObject1_5.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_5.AssocValue = 0
    dimObject1_5.HelpPoint.X = 0.0
    dimObject1_5.HelpPoint.Y = 0.0
    dimObject1_5.HelpPoint.Z = 0.0
    dimObject1_5.View = NXOpen.NXObject.Null
    dimObject2_5 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_5.Geometry = line6
    dimObject2_5.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_5.AssocValue = 0
    dimObject2_5.HelpPoint.X = 0.0
    dimObject2_5.HelpPoint.Y = 0.0
    dimObject2_5.HelpPoint.Z = 0.0
    dimObject2_5.View = NXOpen.NXObject.Null
    dimOrigin5 = NXOpen.Point3d(-4.2481832292704089, -30.0, -7.5)
    sketchDimensionalConstraint5 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_5, dimObject2_5, dimOrigin5, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint4 = sketchDimensionalConstraint5
    dimension5 = sketchHelpedDimensionalConstraint4.AssociatedDimension
    
    expression19 = sketchHelpedDimensionalConstraint4.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    geoms3 = [NXOpen.SmartObject.Null] * 4 
    geoms3[0] = line5
    geoms3[1] = line6
    geoms3[2] = line7
    geoms3[3] = line8
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms3)
    
    geoms4 = [NXOpen.SmartObject.Null] * 4 
    geoms4[0] = line5
    geoms4[1] = line6
    geoms4[2] = line7
    geoms4[3] = line8
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms4)
    
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    theSession.SetUndoMarkVisibility(markId31, "Create Rectangle", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    # Creating rectangle using By 2 Points method 
    # ----------------------------------------------
    startPoint9 = NXOpen.Point3d(10.000000000000004, -30.0, -10.0)
    endPoint9 = NXOpen.Point3d(7.0000000000000053, -30.0, -10.0)
    line9 = workPart.Curves.CreateLine(startPoint9, endPoint9)
    
    startPoint10 = NXOpen.Point3d(7.0000000000000053, -30.0, -10.0)
    endPoint10 = NXOpen.Point3d(7.0000000000000053, -30.0, -5.0)
    line10 = workPart.Curves.CreateLine(startPoint10, endPoint10)
    
    startPoint11 = NXOpen.Point3d(7.0000000000000053, -30.0, -5.0)
    endPoint11 = NXOpen.Point3d(10.000000000000004, -30.0, -5.0)
    line11 = workPart.Curves.CreateLine(startPoint11, endPoint11)
    
    startPoint12 = NXOpen.Point3d(10.000000000000004, -30.0, -5.0)
    endPoint12 = NXOpen.Point3d(10.000000000000004, -30.0, -10.0)
    line12 = workPart.Curves.CreateLine(startPoint12, endPoint12)
    
    theSession.ActiveSketch.AddGeometry(line9, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line10, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line11, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line12, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_10 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_10.Geometry = line9
    geom1_10.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_10.SplineDefiningPointIndex = 0
    geom2_10 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_10.Geometry = line10
    geom2_10.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_10.SplineDefiningPointIndex = 0
    sketchGeometricConstraint22 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_10, geom2_10)
    
    geom1_11 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_11.Geometry = line10
    geom1_11.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_11.SplineDefiningPointIndex = 0
    geom2_11 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_11.Geometry = line11
    geom2_11.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_11.SplineDefiningPointIndex = 0
    sketchGeometricConstraint23 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_11, geom2_11)
    
    geom1_12 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_12.Geometry = line11
    geom1_12.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_12.SplineDefiningPointIndex = 0
    geom2_12 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_12.Geometry = line12
    geom2_12.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_12.SplineDefiningPointIndex = 0
    sketchGeometricConstraint24 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_12, geom2_12)
    
    geom1_13 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_13.Geometry = line12
    geom1_13.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_13.SplineDefiningPointIndex = 0
    geom2_13 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_13.Geometry = line9
    geom2_13.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_13.SplineDefiningPointIndex = 0
    sketchGeometricConstraint25 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_13, geom2_13)
    
    geom7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom7.Geometry = line9
    geom7.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom7.SplineDefiningPointIndex = 0
    sketchGeometricConstraint26 = theSession.ActiveSketch.CreateHorizontalConstraint(geom7)
    
    conGeom1_11 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_11.Geometry = line9
    conGeom1_11.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_11.SplineDefiningPointIndex = 0
    conGeom2_11 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_11.Geometry = line10
    conGeom2_11.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_11.SplineDefiningPointIndex = 0
    sketchGeometricConstraint27 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_11, conGeom2_11)
    
    conGeom1_12 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_12.Geometry = line10
    conGeom1_12.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_12.SplineDefiningPointIndex = 0
    conGeom2_12 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_12.Geometry = line11
    conGeom2_12.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_12.SplineDefiningPointIndex = 0
    sketchGeometricConstraint28 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_12, conGeom2_12)
    
    conGeom1_13 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_13.Geometry = line11
    conGeom1_13.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_13.SplineDefiningPointIndex = 0
    conGeom2_13 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_13.Geometry = line12
    conGeom2_13.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_13.SplineDefiningPointIndex = 0
    sketchGeometricConstraint29 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_13, conGeom2_13)
    
    conGeom1_14 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_14.Geometry = line12
    conGeom1_14.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_14.SplineDefiningPointIndex = 0
    conGeom2_14 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_14.Geometry = line9
    conGeom2_14.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_14.SplineDefiningPointIndex = 0
    sketchGeometricConstraint30 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_14, conGeom2_14)
    
    geom1_14 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_14.Geometry = line9
    geom1_14.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_14.SplineDefiningPointIndex = 0
    geom2_14 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys3 = workPart.Features.FindObject("SKETCH(3:1B)")
    point11 = datumCsys3.FindObject("POINT 1")
    geom2_14.Geometry = point11
    geom2_14.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_14.SplineDefiningPointIndex = 0
    sketchGeometricConstraint31 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_14, geom2_14)
    
    dimObject1_6 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_6.Geometry = line9
    dimObject1_6.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_6.AssocValue = 0
    dimObject1_6.HelpPoint.X = 0.0
    dimObject1_6.HelpPoint.Y = 0.0
    dimObject1_6.HelpPoint.Z = 0.0
    dimObject1_6.View = NXOpen.NXObject.Null
    dimObject2_6 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_6.Geometry = line9
    dimObject2_6.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_6.AssocValue = 0
    dimObject2_6.HelpPoint.X = 0.0
    dimObject2_6.HelpPoint.Y = 0.0
    dimObject2_6.HelpPoint.Z = 0.0
    dimObject2_6.View = NXOpen.NXObject.Null
    dimOrigin6 = NXOpen.Point3d(8.5000000000000036, -30.0, -7.2481832292704054)
    sketchDimensionalConstraint6 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_6, dimObject2_6, dimOrigin6, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint5 = sketchDimensionalConstraint6
    dimension6 = sketchHelpedDimensionalConstraint5.AssociatedDimension
    
    expression20 = sketchHelpedDimensionalConstraint5.AssociatedExpression
    
    dimObject1_7 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_7.Geometry = line10
    dimObject1_7.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_7.AssocValue = 0
    dimObject1_7.HelpPoint.X = 0.0
    dimObject1_7.HelpPoint.Y = 0.0
    dimObject1_7.HelpPoint.Z = 0.0
    dimObject1_7.View = NXOpen.NXObject.Null
    dimObject2_7 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_7.Geometry = line10
    dimObject2_7.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_7.AssocValue = 0
    dimObject2_7.HelpPoint.X = 0.0
    dimObject2_7.HelpPoint.Y = 0.0
    dimObject2_7.HelpPoint.Z = 0.0
    dimObject2_7.View = NXOpen.NXObject.Null
    dimOrigin7 = NXOpen.Point3d(9.7518167707296008, -30.0, -7.5)
    sketchDimensionalConstraint7 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_7, dimObject2_7, dimOrigin7, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint6 = sketchDimensionalConstraint7
    dimension7 = sketchHelpedDimensionalConstraint6.AssociatedDimension
    
    expression21 = sketchHelpedDimensionalConstraint6.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    geoms5 = [NXOpen.SmartObject.Null] * 4 
    geoms5[0] = line9
    geoms5[1] = line10
    geoms5[2] = line11
    geoms5[3] = line12
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms5)
    
    geoms6 = [NXOpen.SmartObject.Null] * 4 
    geoms6[0] = line9
    geoms6[1] = line10
    geoms6[2] = line11
    geoms6[3] = line12
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms6)
    
    # ----------------------------------------------
    #   功能表：檔案(F)->完成草圖(K)
    # ----------------------------------------------
    sketch4 = theSession.ActiveSketch
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   功能表：插入(S)->設計特徵(E)->拉伸(X)...
    # ----------------------------------------------
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    extrudeBuilder2 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder2.Section = section2
    
    extrudeBuilder2.AllowSelfIntersectingSection(True)
    
    expression22 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder2.DistanceTolerance = 0.01
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies2)
    
    extrudeBuilder2.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("30")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies3 = [NXOpen.Body.Null] * 1 
    targetBodies3[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies3)
    
    extrudeBuilder2.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder2.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder2 = extrudeBuilder2.SmartVolumeProfile
    
    smartVolumeProfileBuilder2.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder2.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId33, "拉伸 對話方塊")
    
    section2.DistanceTolerance = 0.01
    
    section2.ChainingTolerance = 0.0094999999999999998
    
    section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    scaleAboutPoint14 = NXOpen.Point3d(-19.287661815277858, -14.812924274133421, 0.0)
    viewCenter14 = NXOpen.Point3d(19.287661815277858, 14.812924274133421, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint14, viewCenter14)
    
    scaleAboutPoint15 = NXOpen.Point3d(-15.430129452222285, -11.850339419306735, 0.0)
    viewCenter15 = NXOpen.Point3d(15.430129452222285, 11.850339419306735, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint15, viewCenter15)
    
    scaleAboutPoint16 = NXOpen.Point3d(-12.344103561777844, -9.4802715354453877, 0.0)
    viewCenter16 = NXOpen.Point3d(12.344103561777844, 9.4802715354453877, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint16, viewCenter16)
    
    scaleAboutPoint17 = NXOpen.Point3d(-9.8752828494222609, -7.5842172283563221, 0.0)
    viewCenter17 = NXOpen.Point3d(9.8752828494222733, 7.5842172283563087, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint17, viewCenter17)
    
    scaleAboutPoint18 = NXOpen.Point3d(-7.900226279537808, -6.0673737826850571, 0.0)
    viewCenter18 = NXOpen.Point3d(7.9002262795378284, 6.0673737826850358, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint18, viewCenter18)
    
    scaleAboutPoint19 = NXOpen.Point3d(-6.320181023630238, -4.8538990261480537, 0.0)
    viewCenter19 = NXOpen.Point3d(6.3201810236302718, 4.8538990261480208, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint19, viewCenter19)
    
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features2 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature2 = feature3
    features2[0] = sketchFeature2
    curveFeatureRule2 = workPart.ScRuleFactory.CreateRuleCurveFeature(features2)
    
    section2.AllowSelfIntersection(True)
    
    rules2 = [None] * 1 
    rules2[0] = curveFeatureRule2
    helpPoint2 = NXOpen.Point3d(8.6101112237933961, -30.0, -5.0)
    section2.AddToSection(rules2, line11, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId35, None)
    
    direction4 = workPart.Directions.CreateDirection(sketch4, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder2.Direction = direction4
    
    targetBodies4 = [NXOpen.Body.Null] * 1 
    body1 = workPart.Bodies.FindObject("EXTRUDE(2)")
    targetBodies4[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies4)
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies5 = [NXOpen.Body.Null] * 1 
    targetBodies5[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies5)
    
    expression23 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression24 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId34, None)
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("10")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies6 = [NXOpen.Body.Null] * 1 
    targetBodies6[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies6)
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies7 = [NXOpen.Body.Null] * 1 
    targetBodies7[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies7)
    
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId36, None)
    
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder2.ParentFeatureInternal = False
    
    feature4 = extrudeBuilder2.CommitFeature()
    
    theSession.DeleteUndoMark(markId37, None)
    
    theSession.SetUndoMarkName(markId33, "拉伸")
    
    expression25 = extrudeBuilder2.Limits.StartExtend.Value
    expression26 = extrudeBuilder2.Limits.EndExtend.Value
    extrudeBuilder2.Destroy()
    
    workPart.Expressions.Delete(expression22)
    
    workPart.Expressions.Delete(expression23)
    
    workPart.Expressions.Delete(expression24)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖(H)...
    # ----------------------------------------------
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchInPlaceBuilder3 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal7 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane7 = workPart.Planes.CreatePlane(origin7, normal7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder3.PlaneReference = plane7
    
    expression27 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression28 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder3 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder3.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId38, "建立草圖 對話方塊")
    
    scalar3 = workPart.Scalars.CreateScalar(1.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge3 = extrude1.FindObject("EDGE * 130 * 160 {(10,-30,10)(10,-30,2.5)(10,-30,-5) EXTRUDE(2)}")
    point12 = workPart.Points.CreatePoint(edge3, scalar3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge4 = extrude1.FindObject("EDGE * 150 * 160 {(10,-30,10)(10,-15,10)(10,0,10) EXTRUDE(2)}")
    direction5 = workPart.Directions.CreateDirection(edge4, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face2 = extrude1.FindObject("FACE 160 {(10,-22.5,0) EXTRUDE(2)}")
    xform3 = workPart.Xforms.CreateXformByPlaneXDirPoint(face2, direction5, point12, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem3 = workPart.CoordinateSystems.CreateCoordinateSystem(xform3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder3.Csystem = cartesianCoordinateSystem3
    
    origin8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal8 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane8 = workPart.Planes.CreatePlane(origin8, normal8, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane8.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom8 = [NXOpen.NXObject.Null] * 1 
    geom8[0] = face2
    plane8.SetGeometry(geom8)
    
    plane8.SetFlip(False)
    
    plane8.SetExpression(None)
    
    plane8.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane8.Evaluate()
    
    origin9 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal9 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane9 = workPart.Planes.CreatePlane(origin9, normal9, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression29 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression30 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane9.SynchronizeToPlane(plane8)
    
    scalar4 = workPart.Scalars.CreateScalar(100.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point13 = workPart.Points.CreatePoint(edge3, scalar4, NXOpen.PointCollection.PointOnCurveLocationOption.PercentParameter, NXOpen.Point.Null, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane9.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom9 = [NXOpen.NXObject.Null] * 1 
    geom9[0] = face2
    plane9.SetGeometry(geom9)
    
    plane9.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane9.Evaluate()
    
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.DeleteUndoMark(markId39, None)
    
    markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject6 = sketchInPlaceBuilder3.Commit()
    
    sketch5 = nXObject6
    feature5 = sketch5.Feature
    
    markId41 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs3 = theSession.UpdateManager.DoUpdate(markId41)
    
    sketch5.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId40, None)
    
    theSession.SetUndoMarkName(markId38, "建立草圖")
    
    sketchInPlaceBuilder3.Destroy()
    
    sketchAlongPathBuilder3.Destroy()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression28)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    workPart.Points.DeletePoint(point13)
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression27)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane7.DestroyPlane()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression30)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression29)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane9.DestroyPlane()
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->圓(C)...
    # ----------------------------------------------
    markId42 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    scaleAboutPoint20 = NXOpen.Point3d(33.855945707382539, 1.6988646591517982, 0.0)
    viewCenter20 = NXOpen.Point3d(-33.855945707382524, -1.6988646591518248, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint20, viewCenter20)
    
    scaleAboutPoint21 = NXOpen.Point3d(27.084756565906037, 1.4238103810034117, 0.0)
    viewCenter21 = NXOpen.Point3d(-27.084756565906027, -1.423810381003433, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint21, viewCenter21)
    
    scaleAboutPoint22 = NXOpen.Point3d(21.667805252724822, 1.190823227748308, 0.0)
    viewCenter22 = NXOpen.Point3d(-21.667805252724815, -1.1908232277483293, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint22, viewCenter22)
    
    scaleAboutPoint23 = NXOpen.Point3d(17.334244202179857, 0.95265858219864286, 0.0)
    viewCenter23 = NXOpen.Point3d(-17.334244202179836, -0.95265858219866328, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint23, viewCenter23)
    
    markId43 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId43, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix1 = theSession.ActiveSketch.Orientation
    
    center1 = NXOpen.Point3d(10.000000000000004, -25.699999999999999, -7.3000000000000007)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 2.6101189014755359, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_8 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_8.Geometry = arc1
    dimObject1_8.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_8.AssocValue = 0
    dimObject1_8.HelpPoint.X = 0.0
    dimObject1_8.HelpPoint.Y = 0.0
    dimObject1_8.HelpPoint.Z = 0.0
    dimObject1_8.View = NXOpen.NXObject.Null
    dimOrigin8 = NXOpen.Point3d(10.000000000000004, -25.699999999999999, -6.92428528356972)
    sketchDimensionalConstraint8 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_8, dimOrigin8, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension8 = sketchDimensionalConstraint8.AssociatedDimension
    
    expression31 = sketchDimensionalConstraint8.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   對話開始 圓
    # ----------------------------------------------
    markId44 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId44, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix2 = theSession.ActiveSketch.Orientation
    
    center2 = NXOpen.Point3d(10.000000000000004, -9.5972502707967173, -7.3000000000000007)
    arc2 = workPart.Curves.CreateArc(center2, nXMatrix2, 3.1142168507222094, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_9 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_9.Geometry = arc2
    dimObject1_9.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_9.AssocValue = 0
    dimObject1_9.HelpPoint.X = 0.0
    dimObject1_9.HelpPoint.Y = 0.0
    dimObject1_9.HelpPoint.Z = 0.0
    dimObject1_9.View = NXOpen.NXObject.Null
    dimOrigin9 = NXOpen.Point3d(10.000000000000004, -9.5972502707967173, -6.92428528356972)
    sketchDimensionalConstraint9 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_9, dimOrigin9, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension9 = sketchDimensionalConstraint9.AssociatedDimension
    
    expression32 = sketchDimensionalConstraint9.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   對話開始 圓
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：插入(S)->草圖約束(K)->尺寸(D)->快速(P)...
    # ----------------------------------------------
    markId45 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchRapidDimensionBuilder4 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines17 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBefore(lines17)
    
    lines18 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAfter(lines18)
    
    lines19 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAbove(lines19)
    
    lines20 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBelow(lines20)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder4.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines21 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBefore(lines21)
    
    lines22 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAfter(lines22)
    
    lines23 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAbove(lines23)
    
    lines24 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBelow(lines24)
    
    theSession.SetUndoMarkName(markId45, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder4.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits73 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits74 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits75 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits76 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits77 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits78 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits79 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits80 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits81 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits82 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder4.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits83 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits84 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits85 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits86 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits87 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits88 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits89 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits90 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits91 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits92 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    point1_5 = NXOpen.Point3d(10.000000000000004, -25.699999999999999, -7.3000000000000007)
    point2_5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_5, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_5)
    
    point1_6 = NXOpen.Point3d(10.000000000000004, -25.699999999999999, -7.3000000000000007)
    point2_6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc1, workPart.ModelingViews.WorkView, point1_6, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_6)
    
    point1_7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_7, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_7)
    
    dimensionlinearunits93 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits94 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits95 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits96 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits97 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits98 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin3 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin3.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin3.View = NXOpen.View.Null
    assocOrigin3.ViewOfGeometry = workPart.ModelingViews.WorkView
    point14 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin3.PointOnGeometry = point14
    assocOrigin3.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin3.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin3.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.DimensionLine = 0
    assocOrigin3.AssociatedView = NXOpen.View.Null
    assocOrigin3.AssociatedPoint = NXOpen.Point.Null
    assocOrigin3.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin3.XOffsetFactor = 0.0
    assocOrigin3.YOffsetFactor = 0.0
    assocOrigin3.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder4.Origin.SetAssociativeOrigin(assocOrigin3)
    
    point15 = NXOpen.Point3d(10.000000000000004, -22.520271038013242, -3.6816810244982037)
    sketchRapidDimensionBuilder4.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point15)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.TextCentered = False
    
    markId46 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject7 = sketchRapidDimensionBuilder4.Commit()
    
    theSession.DeleteUndoMark(markId46, None)
    
    theSession.SetUndoMarkName(markId45, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId45, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder4.Destroy()
    
    markId47 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder5 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines25 = []
    sketchRapidDimensionBuilder5.AppendedText.SetBefore(lines25)
    
    lines26 = []
    sketchRapidDimensionBuilder5.AppendedText.SetAfter(lines26)
    
    lines27 = []
    sketchRapidDimensionBuilder5.AppendedText.SetAbove(lines27)
    
    lines28 = []
    sketchRapidDimensionBuilder5.AppendedText.SetBelow(lines28)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder5.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId47, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder5.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits99 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits100 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits101 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits102 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits103 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits104 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits105 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits106 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits107 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits108 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder5.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits109 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits110 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits111 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits112 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits113 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits114 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits115 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits116 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits117 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits118 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    expression33 = workPart.Expressions.FindObject("p6")
    expression33.SetFormula("3")
    
    theSession.SetUndoMarkVisibility(markId47, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId48 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.Scale(0.574686463192285)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId48, None)
    
    markId49 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId47, "Edit Driving Value")
    
    point1_8 = NXOpen.Point3d(10.000000000000004, -18.274815918726816, -6.3217788653422557)
    point2_8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_8, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_8)
    
    point1_9 = NXOpen.Point3d(10.000000000000004, -18.274815918726816, -6.3217788653422557)
    point2_9 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc2, workPart.ModelingViews.WorkView, point1_9, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_9)
    
    point1_10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_10, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_10)
    
    dimensionlinearunits119 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits120 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits121 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits122 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits123 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits124 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin4 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin4.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin4.View = NXOpen.View.Null
    assocOrigin4.ViewOfGeometry = workPart.ModelingViews.WorkView
    point16 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin4.PointOnGeometry = point16
    assocOrigin4.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin4.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin4.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin4.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin4.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin4.DimensionLine = 0
    assocOrigin4.AssociatedView = NXOpen.View.Null
    assocOrigin4.AssociatedPoint = NXOpen.Point.Null
    assocOrigin4.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin4.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin4.XOffsetFactor = 0.0
    assocOrigin4.YOffsetFactor = 0.0
    assocOrigin4.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder5.Origin.SetAssociativeOrigin(assocOrigin4)
    
    point17 = NXOpen.Point3d(10.000000000000004, -11.784223016017977, -4.0130405313499091)
    sketchRapidDimensionBuilder5.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point17)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.TextCentered = False
    
    markId50 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject8 = sketchRapidDimensionBuilder5.Commit()
    
    theSession.DeleteUndoMark(markId50, None)
    
    theSession.SetUndoMarkName(markId49, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId49, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder5.Destroy()
    
    markId51 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder6 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines29 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBefore(lines29)
    
    lines30 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAfter(lines30)
    
    lines31 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAbove(lines31)
    
    lines32 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBelow(lines32)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder6.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId51, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder6.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits125 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits126 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits127 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits128 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits129 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits130 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits131 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits132 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits133 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits134 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder6.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits135 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits136 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits137 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits138 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits139 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits140 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits141 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits142 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits143 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits144 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    expression34 = workPart.Expressions.FindObject("p7")
    expression34.SetFormula("3.57939653511")
    
    theSession.SetUndoMarkVisibility(markId51, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId52 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId52, None)
    
    markId53 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId51, "Edit Driving Value")
    
    expression34.SetFormula("3")
    
    theSession.SetUndoMarkVisibility(markId53, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId54 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId54, None)
    
    markId55 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId53, "Edit Driving Value")
    
    point1_11 = NXOpen.Point3d(10.000000000000004, -18.274815918726816, -6.3217788653422557)
    point2_11 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_11, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_11)
    
    point1_12 = NXOpen.Point3d(10.000000000000004, -18.274815918726816, -6.3217788653422557)
    point2_12 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc2, workPart.ModelingViews.WorkView, point1_12, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_12)
    
    point1_13 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_13 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_13, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_13)
    
    dimensionlinearunits145 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits146 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits147 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits148 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits149 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits150 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    point18 = NXOpen.Point3d(10.000000000000004, 0.0, -6.8295963395894104)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(line3, workPart.ModelingViews.WorkView, point18)
    
    point1_14 = NXOpen.Point3d(10.000000000000004, 0.0, -6.8295963395894104)
    point2_14 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line3, workPart.ModelingViews.WorkView, point1_14, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_14)
    
    point1_15 = NXOpen.Point3d(10.000000000000004, -18.274815918726816, -6.3217788653422557)
    point2_15 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_15, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_15)
    
    point1_16 = NXOpen.Point3d(10.000000000000004, 0.0, -6.8295963395894104)
    point2_16 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line3, workPart.ModelingViews.WorkView, point1_16, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_16)
    
    point1_17 = NXOpen.Point3d(10.000000000000004, -18.274815918726816, -6.3217788653422557)
    point2_17 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_17, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_17)
    
    dimensionlinearunits151 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits152 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits153 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits154 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits155 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits156 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits157 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits158 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits159 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits160 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits161 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits162 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin5 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin5.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin5.View = NXOpen.View.Null
    assocOrigin5.ViewOfGeometry = workPart.ModelingViews.WorkView
    point19 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin5.PointOnGeometry = point19
    assocOrigin5.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin5.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin5.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin5.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin5.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin5.DimensionLine = 0
    assocOrigin5.AssociatedView = NXOpen.View.Null
    assocOrigin5.AssociatedPoint = NXOpen.Point.Null
    assocOrigin5.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin5.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin5.XOffsetFactor = 0.0
    assocOrigin5.YOffsetFactor = 0.0
    assocOrigin5.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder6.Origin.SetAssociativeOrigin(assocOrigin5)
    
    point20 = NXOpen.Point3d(10.000000000000004, -3.3014196406143084, -12.661523660179434)
    sketchRapidDimensionBuilder6.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point20)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.TextCentered = False
    
    markId56 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject9 = sketchRapidDimensionBuilder6.Commit()
    
    theSession.DeleteUndoMark(markId56, None)
    
    theSession.SetUndoMarkName(markId55, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId55, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder6.Destroy()
    
    markId57 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder7 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines33 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBefore(lines33)
    
    lines34 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAfter(lines34)
    
    lines35 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAbove(lines35)
    
    lines36 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBelow(lines36)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder7.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId57, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder7.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits163 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits164 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits165 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits166 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits167 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits168 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits169 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits170 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits171 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits172 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder7.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits173 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits174 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits175 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits176 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits177 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits178 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits179 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits180 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits181 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits182 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    expression35 = workPart.Expressions.FindObject("p8")
    expression35.SetFormula("5")
    
    theSession.SetUndoMarkVisibility(markId57, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId58 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId58, None)
    
    markId59 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId57, "Edit Driving Value")
    
    point1_18 = NXOpen.Point3d(10.000000000000004, -5.0, -6.3217788653422557)
    point2_18 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_18, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_18)
    
    point1_19 = NXOpen.Point3d(10.000000000000004, -5.0, -6.3217788653422557)
    point2_19 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc2, workPart.ModelingViews.WorkView, point1_19, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_19)
    
    point1_20 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_20 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_20, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_20)
    
    dimensionlinearunits183 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits184 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits185 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits186 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits187 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits188 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    edge5 = extrude1.FindObject("EDGE * 160 * 170 {(10,-45,-10)(10,-22.5,-10)(10,0,-10) EXTRUDE(2)}")
    point21 = NXOpen.Point3d(10.000000000000004, -4.2954981611694265, -10.0)
    sketchRapidDimensionBuilder7.SecondAssociativity.SetValue(edge5, workPart.ModelingViews.WorkView, point21)
    
    point1_21 = NXOpen.Point3d(10.000000000000004, -4.2954981611694265, -10.0)
    point2_21 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge5, workPart.ModelingViews.WorkView, point1_21, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_21)
    
    point1_22 = NXOpen.Point3d(10.000000000000004, -5.0, -6.3217788653422557)
    point2_22 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_22, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_22)
    
    point1_23 = NXOpen.Point3d(10.000000000000004, -4.2954981611694265, -10.0)
    point2_23 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge5, workPart.ModelingViews.WorkView, point1_23, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_23)
    
    point1_24 = NXOpen.Point3d(10.000000000000004, -5.0, -6.3217788653422557)
    point2_24 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_24, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_24)
    
    dimensionlinearunits189 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits190 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits191 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits192 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits193 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits194 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits195 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits196 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits197 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits198 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits199 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits200 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin6 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin6.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin6.View = NXOpen.View.Null
    assocOrigin6.ViewOfGeometry = workPart.ModelingViews.WorkView
    point22 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin6.PointOnGeometry = point22
    assocOrigin6.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin6.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin6.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin6.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin6.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin6.DimensionLine = 0
    assocOrigin6.AssociatedView = NXOpen.View.Null
    assocOrigin6.AssociatedPoint = NXOpen.Point.Null
    assocOrigin6.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin6.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin6.XOffsetFactor = 0.0
    assocOrigin6.YOffsetFactor = 0.0
    assocOrigin6.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder7.Origin.SetAssociativeOrigin(assocOrigin6)
    
    point23 = NXOpen.Point3d(10.000000000000004, 3.5908581019011692, -8.6852095779589646)
    sketchRapidDimensionBuilder7.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point23)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.TextCentered = False
    
    markId60 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject10 = sketchRapidDimensionBuilder7.Commit()
    
    theSession.DeleteUndoMark(markId60, None)
    
    theSession.SetUndoMarkName(markId59, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId59, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder7.Destroy()
    
    markId61 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder8 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines37 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBefore(lines37)
    
    lines38 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAfter(lines38)
    
    lines39 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAbove(lines39)
    
    lines40 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBelow(lines40)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder8.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId61, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder8.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits201 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits202 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits203 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits204 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits205 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits206 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits207 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits208 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits209 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits210 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder8.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits211 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits212 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits213 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits214 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits215 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits216 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits217 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits218 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits219 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits220 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    expression36 = workPart.Expressions.FindObject("p9")
    expression36.SetFormula("3")
    
    theSession.SetUndoMarkVisibility(markId61, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId62 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId62, None)
    
    markId63 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId61, "Edit Driving Value")
    
    point1_25 = NXOpen.Point3d(10.000000000000004, -5.0, -7.0)
    point2_25 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_25, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_25)
    
    point1_26 = NXOpen.Point3d(10.000000000000004, -5.0, -7.0)
    point2_26 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc2, workPart.ModelingViews.WorkView, point1_26, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_26)
    
    point1_27 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_27 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_27, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_27)
    
    dimensionlinearunits221 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits222 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits223 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits224 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits225 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits226 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    point1_28 = NXOpen.Point3d(10.000000000000004, -27.528848208273175, -6.3217788653422557)
    point2_28 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_28, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_28)
    
    point1_29 = NXOpen.Point3d(10.000000000000004, -5.0, -7.0)
    point2_29 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_29, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_29)
    
    point1_30 = NXOpen.Point3d(10.000000000000004, -27.528848208273175, -6.3217788653422557)
    point2_30 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_30, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_30)
    
    point1_31 = NXOpen.Point3d(10.000000000000004, -5.0, -7.0)
    point2_31 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_31, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_31)
    
    point1_32 = NXOpen.Point3d(10.000000000000004, -27.528848208273175, -6.3217788653422557)
    point2_32 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_32, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_32)
    
    dimensionlinearunits227 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits228 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits229 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits230 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits231 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits232 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits233 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits234 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits235 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits236 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits237 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits238 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin7 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin7.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin7.View = NXOpen.View.Null
    assocOrigin7.ViewOfGeometry = workPart.ModelingViews.WorkView
    point24 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin7.PointOnGeometry = point24
    assocOrigin7.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin7.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin7.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin7.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin7.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin7.DimensionLine = 0
    assocOrigin7.AssociatedView = NXOpen.View.Null
    assocOrigin7.AssociatedPoint = NXOpen.Point.Null
    assocOrigin7.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin7.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin7.XOffsetFactor = 0.0
    assocOrigin7.YOffsetFactor = 0.0
    assocOrigin7.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder8.Origin.SetAssociativeOrigin(assocOrigin7)
    
    point25 = NXOpen.Point3d(10.000000000000004, -21.261104911976759, -16.107662531437175)
    sketchRapidDimensionBuilder8.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point25)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.TextCentered = False
    
    markId64 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject11 = sketchRapidDimensionBuilder8.Commit()
    
    theSession.DeleteUndoMark(markId64, None)
    
    theSession.SetUndoMarkName(markId63, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId63, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder8.Destroy()
    
    markId65 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder9 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines41 = []
    sketchRapidDimensionBuilder9.AppendedText.SetBefore(lines41)
    
    lines42 = []
    sketchRapidDimensionBuilder9.AppendedText.SetAfter(lines42)
    
    lines43 = []
    sketchRapidDimensionBuilder9.AppendedText.SetAbove(lines43)
    
    lines44 = []
    sketchRapidDimensionBuilder9.AppendedText.SetBelow(lines44)
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder9.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId65, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder9.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits239 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits240 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits241 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits242 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits243 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits244 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits245 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits246 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits247 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits248 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder9.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits249 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits250 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits251 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits252 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits253 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits254 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits255 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits256 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits257 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits258 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    expression37 = workPart.Expressions.FindObject("p10")
    expression37.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId65, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId66 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId66, None)
    
    markId67 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId65, "Edit Driving Value")
    
    point1_33 = NXOpen.Point3d(10.000000000000004, -25.0, -6.3217788653422557)
    point2_33 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_33, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_33)
    
    point1_34 = NXOpen.Point3d(10.000000000000004, -25.0, -6.3217788653422557)
    point2_34 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc1, workPart.ModelingViews.WorkView, point1_34, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_34)
    
    point1_35 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_35 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_35, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_35)
    
    dimensionlinearunits259 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits260 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits261 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits262 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits263 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits264 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    point26 = NXOpen.Point3d(10.000000000000004, -23.514349558568355, -10.0)
    sketchRapidDimensionBuilder9.SecondAssociativity.SetValue(edge5, workPart.ModelingViews.WorkView, point26)
    
    point1_36 = NXOpen.Point3d(10.000000000000004, -23.514349558568355, -10.0)
    point2_36 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge5, workPart.ModelingViews.WorkView, point1_36, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_36)
    
    point1_37 = NXOpen.Point3d(10.000000000000004, -25.0, -6.3217788653422557)
    point2_37 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_37, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_37)
    
    point1_38 = NXOpen.Point3d(10.000000000000004, -23.514349558568355, -10.0)
    point2_38 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge5, workPart.ModelingViews.WorkView, point1_38, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_38)
    
    point1_39 = NXOpen.Point3d(10.000000000000004, -25.0, -6.3217788653422557)
    point2_39 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_39, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_39)
    
    dimensionlinearunits265 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits266 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits267 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits268 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits269 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits270 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits271 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits272 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits273 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits274 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits275 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits276 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin8 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin8.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin8.View = NXOpen.View.Null
    assocOrigin8.ViewOfGeometry = workPart.ModelingViews.WorkView
    point27 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin8.PointOnGeometry = point27
    assocOrigin8.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin8.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin8.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin8.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin8.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin8.DimensionLine = 0
    assocOrigin8.AssociatedView = NXOpen.View.Null
    assocOrigin8.AssociatedPoint = NXOpen.Point.Null
    assocOrigin8.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin8.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin8.XOffsetFactor = 0.0
    assocOrigin8.YOffsetFactor = 0.0
    assocOrigin8.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder9.Origin.SetAssociativeOrigin(assocOrigin8)
    
    point28 = NXOpen.Point3d(10.000000000000004, -18.809044561274135, -8.8508893313848169)
    sketchRapidDimensionBuilder9.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point28)
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.TextCentered = False
    
    markId68 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject12 = sketchRapidDimensionBuilder9.Commit()
    
    theSession.DeleteUndoMark(markId68, None)
    
    theSession.SetUndoMarkName(markId67, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId67, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder9.Destroy()
    
    markId69 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder10 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines45 = []
    sketchRapidDimensionBuilder10.AppendedText.SetBefore(lines45)
    
    lines46 = []
    sketchRapidDimensionBuilder10.AppendedText.SetAfter(lines46)
    
    lines47 = []
    sketchRapidDimensionBuilder10.AppendedText.SetAbove(lines47)
    
    lines48 = []
    sketchRapidDimensionBuilder10.AppendedText.SetBelow(lines48)
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder10.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder10.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder10.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId69, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder10.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits277 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits278 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits279 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits280 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits281 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits282 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits283 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits284 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits285 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits286 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder10.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder10.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits287 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits288 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits289 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits290 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits291 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits292 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits293 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits294 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits295 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits296 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    expression38 = workPart.Expressions.FindObject("p11")
    expression38.SetFormula("3")
    
    theSession.SetUndoMarkVisibility(markId69, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId70 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId70, None)
    
    markId71 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId69, "Edit Driving Value")
    
    # ----------------------------------------------
    #   功能表：檔案(F)->完成草圖(K)
    # ----------------------------------------------
    sketchRapidDimensionBuilder10.Destroy()
    
    theSession.UndoToMark(markId71, None)
    
    theSession.DeleteUndoMark(markId71, None)
    
    sketchRapidDimensionBuilder10.Destroy()
    
    sketch6 = theSession.ActiveSketch
    
    markId72 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   功能表：插入(S)->設計特徵(E)->拉伸(X)...
    # ----------------------------------------------
    markId73 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    extrudeBuilder3 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section3 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder3.Section = section3
    
    extrudeBuilder3.AllowSelfIntersectingSection(True)
    
    expression39 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder3.DistanceTolerance = 0.01
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies8 = [NXOpen.Body.Null] * 1 
    targetBodies8[0] = NXOpen.Body.Null
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies8)
    
    extrudeBuilder3.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies9 = [NXOpen.Body.Null] * 1 
    targetBodies9[0] = NXOpen.Body.Null
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies9)
    
    extrudeBuilder3.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder3.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder3.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder3.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder3 = extrudeBuilder3.SmartVolumeProfile
    
    smartVolumeProfileBuilder3.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder3.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId73, "拉伸 對話方塊")
    
    section3.DistanceTolerance = 0.01
    
    section3.ChainingTolerance = 0.0094999999999999998
    
    section3.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId74 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId75 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features3 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature3 = feature5
    features3[0] = sketchFeature3
    curveFeatureRule3 = workPart.ScRuleFactory.CreateRuleCurveFeature(features3)
    
    section3.AllowSelfIntersection(True)
    
    rules3 = [None] * 1 
    rules3[0] = curveFeatureRule3
    helpPoint3 = NXOpen.Point3d(10.000000000000004, -23.504715842580069, -7.0054076663768683)
    section3.AddToSection(rules3, arc1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint3, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId75, None)
    
    direction6 = workPart.Directions.CreateDirection(sketch6, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder3.Direction = direction6
    
    targetBodies10 = [NXOpen.Body.Null] * 1 
    targetBodies10[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies10)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies11 = [NXOpen.Body.Null] * 1 
    targetBodies11[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies11)
    
    expression40 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression41 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId74, None)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies12 = [NXOpen.Body.Null] * 1 
    targetBodies12[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies12)
    
    direction7 = extrudeBuilder3.Direction
    
    success1 = direction7.ReverseDirection()
    
    extrudeBuilder3.Direction = direction7
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("32")
    
    markId76 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId76, None)
    
    markId77 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder3.ParentFeatureInternal = False
    
    feature6 = extrudeBuilder3.CommitFeature()
    
    theSession.DeleteUndoMark(markId77, None)
    
    theSession.SetUndoMarkName(markId73, "拉伸")
    
    expression42 = extrudeBuilder3.Limits.StartExtend.Value
    expression43 = extrudeBuilder3.Limits.EndExtend.Value
    extrudeBuilder3.Destroy()
    
    workPart.Expressions.Delete(expression39)
    
    workPart.Expressions.Delete(expression40)
    
    workPart.Expressions.Delete(expression41)
    
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = -0.081359777914642994
    rotMatrix1.Xy = 0.98003297522652155
    rotMatrix1.Xz = -0.18142754478394649
    rotMatrix1.Yx = -0.26935907985333746
    rotMatrix1.Yy = 0.15363688381164853
    rotMatrix1.Yz = 0.95070573472195175
    rotMatrix1.Zx = 0.95959693238267607
    rotMatrix1.Zy = 0.12621836396220951
    rotMatrix1.Zz = 0.25148091768653236
    translation1 = NXOpen.Point3d(18.831155374295797, 9.0547700651531073, 16.003506974369667)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 3.2705665928526968)
    
    # ----------------------------------------------
    #   功能表：檔案(F)->另存新檔(A)...
    # ----------------------------------------------
    partSaveStatus1 = workPart.SaveAs("E:\\tuan\\car")
    
    partSaveStatus1.Dispose()
    # ----------------------------------------------
    #   功能表：工具(T)->動作記錄(J)->停止錄製(S)
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()