from flask import Flask, render_template, request
import hirschbergLocalAlignment, utility, linearSpaceCounting, tracebackAll

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/compute', methods = ['POST'])
def compute():
    sequence1 = request.form.get("sequence1")
    sequence2= request.form.get("sequence2")
    delta = hirschbergLocalAlignment.delta
    local_alignment = hirschbergLocalAlignment.linear_space_local_align_solution(sequence1, sequence2, delta)
    best_score = utility.computeScore(local_alignment[0], local_alignment[1], delta)
    num_of_alignment = linearSpaceCounting.linear_space_local_align(sequence1, sequence2, delta)
    tracebackAll.list.clear()
    tracebackAll.local_align(sequence1, sequence2, delta)
    return render_template('index.html', local_alignment=local_alignment, best_score=best_score, num_of_alignment=num_of_alignment, all_alignments=tracebackAll.list)