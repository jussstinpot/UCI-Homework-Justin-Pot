Sub yearlystock():

'To run the entire through all tabs in worksheet
For Each ws In Worksheets

    'Inserting Header Data
    ws.Cells(1, 9).Value = "Ticker"
    ws.Cells(1, 10).Value = "Yearly Change"
    ws.Cells(1, 11).Value = "Percent Change"
    ws.Cells(1, 12).Value = "Total Stock Volume"
'-------------------------------------------------------------------------------------------

    'Insert Bonus Header Data
    ws.cells(1,16).value = "Ticker"
    ws.cells(1,17).value = "Value"
    ws.cells(2,15).value = "Greatest % Increase"
    ws.cells(3,15).value = "Greatest % Decrease"
    ws.cells(4,15).value = "Greatest Total Volume"

'-------------------------------------------------------------------------------------------

'Assigning variables
    Dim i As Long
    Dim ticker As String

    Dim yearly_open As Double
    yearly_open = 0

    Dim yearly_close As Double
    yearly_close = 0

    Dim total_stock_volume As Double
    total_stock_volume = 0

    'yearly close - yearly open
    Dim yearly_change As Double
    yearly_change = 0

    Dim percent_change As Double

    'generate data starting on row 2 because row 1 already has headers printed
    Dim summary_row As Long
    summary_row = 2

    'row count to last row
    Dim last_row As Long
    last_row = ws.Cells(Rows.Count, 1).End(xlUp).Row
'----------------------------------------------------------------------------------------------
        ' Start opening price with a reference point
        yearly_open = ws.Cells(2, 3).Value

        'Begin for loop for variables
        For i = 2 To last_row

            'Cycle through ticker values and when it does not match print next value
            If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then

                'set the ticker name
                ticker = ws.Cells(i, 1).Value

                'Calculating yearly price change and percent change
                yearly_close = ws.Cells(i, 6).Value
                yearly_change = yearly_close - yearly_open

                If yearly_open <> 0 Then
                    percent_change = (yearly_change / yearly_open) * 100
                                 
                    'calulating total Volume
                    total_stock_volume = total_stock_volume + ws.Cells(i, 7).Value

            

'-------------------------------------------------------------------------------------------------
                    'PRINTING RANGES

                 'print ticker name
                    ws.Range("I" & summary_row).Value = ticker

                    'print  yearly change
                    ws.Range("J" & summary_row).Value = yearly_change

                    'print yearly percent change
                    ws.Range("K" & summary_row).Value = (Str(percent_change) & "%")

                    'print total Volume
                    ws.Range("L" & summary_row).Value = total_stock_volume

                    ' Print next row in summary table
                    summary_row = summary_row + 1

                    'start over at 0 for next tickers
                    yearly_change = 0
                    yearly_close = 0
                    yearly_open = ws.Cells(i + 1, 3).Value
                    percent_change = 0
                    total_stock_volume = 0

                End If

            else
                total_stock_volume = total_stock_volume + ws.Cells(i, 7).Value

            End If      

        next I

    'Assigning Variables for Bonus Data
    Dim percent_max as Double
    percent_max = 0

    Dim percent_min as Double
    percent_min = 0
    
    Dim percent_last_row as Long
    percent_last_row = ws.Cells(Rows.Count, 11).End(xlUp).Row
        'Bonus data
        for i = 2 to percent_last_row

            if percent_max < ws.cells(i,11).value Then
                percent_max = ws.cells(i,11).value 
                ws.cells(2,17).value = (str(percent_max * 100) & "%")
                ws.cells(2,16).value = ws.cells(i,9).value
            elseif percent_min > ws.cells(i,11).value Then 
                percent_min = ws.cells(i,11).value 
                ws.cells(3,17).value = (str(percent_min * 100) & "%")
                ws.cells(3,16).value = ws.cells(i,9).value
            end if
        next i
    Dim high_volume as Double
    high_volume = 0

    Dim volume_last_row as Long
    volume_last_row = ws.Cells(Rows.Count, 12).End(xlUp).Row
        for i = 2 to volume_last_row

            if high_volume < ws.cells(i,12).value Then
                high_volume = ws.cells(i,12).value
                ws.cells(4,17).value = high_volume
                ws.cells(4,16).value = ws.cells(i,9).value
            end if
        

        'ADDING Color

        If ws.Cells(i, 10).Value >= 0 Then
            ws.Cells(i, 10).Interior.ColorIndex = 4
        else
            ws.Cells(i, 10).Interior.ColorIndex = 3
        End if
        Next i  
Next ws
End Sub

'----