#!/usr/bin/python3

"""
Launch :  ./keyserver.py
Follow the displayed URL.
Add #debug at the url end to display stats.
"""

# pylint: disable=no-member,len-as-condition,undefined-variable

def rand_range(minimum, maximum):
    """Returns a number in the range minimum...maximum-1"""
    value = int(Date().getTime() + 1000000000 * Math.random() + rand_range.more)
    rand_range.more += Date().getTime()
    return value % (maximum - minimum) + minimum
rand_range.more = 0

def random_int(nr_digits):
    """Returns a number in 100...999 included"""
    return rand_range(10 ** (nr_digits-1), 10 ** nr_digits)

EVEN = "BCDFGHJKLMNPQRSTVWXZ"
ODD = "AEIOUY"
def random_txt(nr_letters):
    """Returns a string"""
    letters = ''
    while nr_letters > 0:
        letters += EVEN[rand_range(0, len(EVEN))]
        if nr_letters > 1:
            letters += ODD[rand_range(0, len(ODD))]
        nr_letters -= 2
    return letters

def add_random(values, nr_digits):
    """Add a random number without duplicate"""
    while True:
        if nr_digits > 0:
            nombre = random_int(nr_digits)
        else:
            nombre = random_txt(-nr_digits)
        if nombre not in values:
            append(values, nombre)
            return

def string(obj):
    """Emulate str on JS"""
    try:
        return obj.toString()
    except: # Python # pylint: disable=bare-except
        return obj.__str__()

def append(array, element):
    """Emulate append on JS"""
    try:
        return array.push(element)
    except: # Python # pylint: disable=bare-except
        return array.append(element)

def join(array):
    """Concatenate the array strings"""
    try:
        return ''.join(array)
    except: # Python # pylint: disable=bare-except
        return array.join('')

def millisec():
    """Current time in millisecs"""
    return Date().getTime() # pylint: disable=undefined-variable

def get_by_id(the_id):
    """Get the HTML element"""
    return document.getElementById(the_id) # pylint: disable=undefined-variable

#############################################################################
#############################################################################
# Test root class
#############################################################################
#############################################################################

class Test:
    """Common part for the tests"""
    values = [] # The values to choose
    start_time = 0. # The display start time
    page = None # The HTML element
    input = None # The HTML element
    style = None # The HTML element
    name = None
    icon = ''
    digits = 1

    def __init__(self, phases):
        self.tests = phases
        self.nr_done = -1
        self.times = [] # Negative if bad answer

    def start(self):
        """Start the test"""
        self.style = get_by_id('style')
        self.page = get_by_id('page')
        self.page.innerHTML = self.html()
        setTimeout('''
            if (document.getElementById("cursor"))
                document.getElementById("cursor").className += " move"
                ''', 100)
        window.onclick = self.onclick.bind(self)
        window.onkeypress = self.onkeypress.bind(self)
        window.ontouchmove = False
        window.ontouchstart = False
        self.terminate_init()
        self.start_time = millisec()
    def html(self):
        """Initialise the random number and generate the page"""
        if self.nr_done == -1:
            return '<h2>' + self.name + ' ' + self.icon + '</h2>' + self.before()
        if self.nr_done == 0:
            self.values = []
            for _ in range(self.tests.nr_tests):
                add_random(self.values, self.tests.nr_digits * self.digits)
        numbers = '<div id="numbers" class="numbers">'
        for i, value in enumerate(self.values):
            if i < self.nr_done:
                if self.times[i] < 0:
                    classe = 'bad'
                else:
                    classe = 'good'
            elif i == self.nr_done:
                numbers += '<span id="cursor" class="cursor">▲</span>'
                classe = 'current'
            else:
                classe = 'future'
            numbers += '<span class="' + classe + '">' + string(value) + '</span>\n'
        numbers += '</div>'
        return self.top() + numbers + self.bottom()
    def answer(self, value):
        """Analyse the user answer and record starts"""
        if self.nr_done >= 0:
            time = millisec() - self.start_time
            if string(value).toLowerCase() != string(self.values[self.nr_done]).toLowerCase():
                time = -time
            append(self.times, time)
        self.nr_done += 1
        if self.nr_done == self.tests.nr_tests:
            self.done()
        else:
            self.start()
    def done(self):
        """The current test ended"""
        self.tests.done()
    def stats(self):
        """Returns [nr tests, nr good answers, average time for good answer]"""
        if self.tests.debug and self.tests.stats:
            # Get values from server stats
            infos = self.tests.stats.data[self.tests.nr_digits][-1]
            return [self.tests.nr_tests - 1, infos[2][self.index],
                    infos[0][self.index], infos[1][self.index]]
        # Stats for the current game
        summ = 0
        summ2 = 0
        goods = []
        for time in self.times[1:]:
            if time > 0:
                append(goods, time)
                summ += time
                summ2 += time * time
        if len(goods):
            average = summ / len(goods)
            stddev = (summ2 / len(goods) - average * average) ** 0.5
        else:
            average = stddev = '?'
        return [len(self.times) - 1, len(goods), average, stddev]

    def before(self): # pylint: disable=no-self-use
        """Before the test"""
        return ''
    def top(self): # pylint: disable=no-self-use
        """Top of the page"""
        return ''
    def bottom(self): # pylint: disable=no-self-use
        """Bottom of the page"""
        return ''
    def onclick(self, event): # pylint: disable=no-self-use
        """Manage the event"""
        print(event)
    def onkeypress(self, event): # pylint: disable=no-self-use
        """Manage the event"""
        print(event)
    def terminate_init(self): # pylint: disable=no-self-use
        """Called when HTML is parsed"""

#############################################################################
#############################################################################
# The possible tests
#############################################################################
#############################################################################

class Welcome(Test):
    """The front page"""
    def html(self):
        return """
        <p>
        Ceci est un test de vitesse d'utilisation du clavier et de la souris.<br>
        On ne peut donc pas le faire sur un téléphone portable ou une tablette.
        <p>
        Choisissez la taille des buttons pour cliquer :
        <p>
        <button style="font-size:16px">Petit</button>
        <button style="font-size:20px" id="button">Normal</button>
        <button style="font-size:24px">Grand</button>
        <button style="font-size:32px">Enorme</button>
        <button style="font-size:48px">Huge</button>
        <p>
        A la fin de l'ensemble des tests vous connaîtrez la méthode de saisie<br>
        pour laquelle vous êtes le plus efficace,
        ainsi que vos classements.
        <p>
        Pour chacun des tests il faudra saisir
        """ + string(self.tests.nr_tests) + """ valeurs de
        """ + string(self.tests.nr_digits) + """ caractères.<br>
        La première saisie ne compte pas dans les statistiques.<br>
        L'ensemble des tests dure environ 3 minutes.
        <p>
        Pour ne pas enregistrer vos résultats :<br>
        rechargez la page avant de finir le dernier test.
        <p>
        Et maintenant, cliquez sur : <button>Je veux commencer !</button>
        <p>
        <table>""" + join(['<tr><td>' + test.name + '<td>' + test.icon + '</tr>'
                           for test in self.tests.phases[1:-1]]) + '</table>'
    def onclick(self, event):
        if event.target.tagName != 'BUTTON':
            return
        size = event.target.style.fontSize
        if size:
            self.style.textContent = 'BUTTON, INPUT, TD, TH, BODY, P { font-size:' + size + '}'
            return
        self.done()
    def onkeypress(self, _event):
        self.done()
    def terminate_init(self):
        self.onclick({'target': get_by_id('button')})

class End(Test):
    """The end page"""
    def html(self):
        self.tests.record()
        return self.tests.resume()

def create_icon(nr_buttons):
    """Create a list of digit"""
    numbers = range(nr_buttons)
    return '<div class="keypad">' + join(['<span>' + string(i) + '</span> '
                                          for i in numbers]) + '</div>'

class Buttons10(Test):
    """The user clicks on a button with the good value"""
    name = 'Buttons10'
    icon = create_icon(10)
    buttons = []
    def before(self):
        return """Prenez la souris.
<p>Vous allez devoir cliquer sur des boutons<br>
Les valeurs des boutons sont triées de la plus petite à la plus grande.
<p>Cliquez n'importe où pour démarrer le test."""
    def top(self):
        return "Cliquez sur le bouton correspondant à la valeur :\n"
    def bottom(self):
        if self.nr_done == 0:
            values = []
            for value in self.values:
                append(values, value)
            while len(values) < int(self.name[-2:]):
                add_random(values, self.tests.nr_digits * self.digits)
            values.sort()
            self.buttons = values
        return join(['<button>' + string(i) + '</button> ' for i in self.buttons])
    def onclick(self, event):
        """Event management"""
        if self.nr_done == -1:
            self.answer('')
        else:
            target = event.target
            if target.tagName == 'BUTTON':
                self.answer(target.textContent)

class ButtonsText10(Buttons10):
    """Letters in place of digits"""
    name = 'ButtonsText10'
    digits = -1

class Buttons20(Buttons10):
    """The user clicks on a button with the good value"""
    name = 'Buttons20'
    icon = create_icon(20)

class ButtonsText20(Buttons20):
    """Letters in place of digits"""
    name = 'ButtonsText20'
    digits = -1

class Buttons40(Buttons10):
    """The user clicks on a button with the good value"""
    name = 'Buttons40'
    icon = create_icon(40)

class ButtonsText40(Buttons40):
    """Letters in place of digits"""
    name = 'ButtonsText40'
    digits = -1

class Keypad(Test):
    """The user clicks on a button with the good value"""
    name = 'Keypad'
    icon = '''
    <div class="keypad"><span>7</span><span>8</span><span>9</span><br>
    <span>4</span><span>5</span><span>6</span><br>
    <span>1</span><span>2</span><span>3</span><br>
    <span>0</span><span>Entrée</span>
    </div>'''
    def before(self):
        return """Prenez la souris.
<p>Vous allez devoir cliquer sur les boutons d'un clavier numérique virtuel.<br>
Il faudra terminer la saisie de la valeur en cliquant sur «Entrée».
<p>Cliquez n'importe où pour démarrer le test."""
    def top(self):
        return "Saisir la valeur jaune puis cliquez sur «Entrée» :\n"
    def bottom(self):
        return '''
Votre saisie :<br><span id="input"></span><button class="b">←</button> <br>
<button class="b">7</button><button class="b">8</button><button class="b">9</button><br>
<button class="b">4</button><button class="b">5</button><button class="b">6</button><br>
<button class="b">1</button><button class="b">2</button><button class="b">3</button><br>
<button class="b">0</button><button class="b" style="width:3.5em;padding:0px">Entrée</button>'''
    def terminate_init(self):
        self.input = get_by_id('input')
    def onclick(self, event):
        """Event management"""
        if self.nr_done == -1:
            self.answer('')
        else:
            target = event.target
            if target.tagName == 'BUTTON':
                if target.textContent in '0123456789':
                    self.input.textContent += target.textContent
                elif target.textContent == '←':
                    self.input.textContent = self.input.textContent.substr(
                        0, self.input.textContent.length-1)
                elif target.textContent == 'Entrée':
                    self.answer(self.input.textContent)

class Keyboard(Test):
    """The user clicks on a button with the good value"""
    name = 'Keyboard'
    icon = '<span class="emoji" style="font-size:200%">⌨</span>'
    def before(self):
        if self.digits == -1:
            more = "<br>PAS BESOIN D'ÉCRIRE EN MAJUSCULE"
        else:
            more = ""
        return """Lachez la souris.
<p>Vous allez devoir saisir des valeurs au clavier.""" + more + """
<p>Appuyez sur une touche pour démarrer le test."""
    def top(self):
        return """Saisissez la valeur affichée en utilisant le clavier<br>
        puis validez avec la touche entrée :\n"""
    def bottom(self):
        return '<input id="input">'
    def onkeypress(self, event):
        if self.nr_done == -1:
            self.answer('')
        elif event.key == 'Enter':
            self.answer(self.input.value)
    def terminate_init(self):
        self.input = get_by_id('input')
        if self.input:
            self.input.focus()

class KeyboardText(Keyboard):
    """Letters in place of digits"""
    name = 'KeyboardText'
    digits = -1

#############################################################################
#############################################################################
# Stats explorer
#############################################################################
#############################################################################

class Stats:
    """Statistics explorer"""
    def __init__(self, data, tests):
        self.data = JSON.parse(data)
        self.tests = tests
    def html(self):
        """Generate the HTML"""
        setTimeout(self.draw.bind(self), 10)
        return '''<style>BODY { margin-left: 0px }</style>
        <div class="box plot"><p>
        Chaque point représente ''' + (self.tests.nr_tests - 1) + '''
        saisies de valeurs <b>sans erreur</b>.<br>
        Couleur : méthode de saisie.<br>
        Bords noirs : les tests que vous venez de faire.
        <p>
        <canvas id="canvas" width="1000" height="1000"
                style="width:var(--width);height:var(--width)"></canvas>
        </div>
        '''
    def update_rank(self): # pylint: disable=too-many-locals,too-many-branches,too-many-statements
        """Update the rank of the result"""
        tests = self.data[self.tests.nr_digits]
        my_id = tests[-1][3]
        for test in self.tests.phases:
            if not test.name:
                continue
            nbr = 0
            my_nbr = 0
            my_errors = 0
            i = test.index
            sum_avg = 0
            sum_stddev = 0
            my_sum_avg = 0
            my_sum_stddev = 0
            sum_percent = 0
            my_sum_percent = 0
            values = []
            for results in tests:
                if results[2][i] == self.tests.nr_tests - 1:
                    nbr += 1
                    sum_avg += results[0][i]
                    sum_stddev += results[1][i]
                    append(values, results[0][i])
                    sum_percent += 100
                    if results[3] == my_id:
                        my_sum_avg += results[0][i]
                        my_sum_stddev += results[1][i]
                        my_sum_percent += 100
                        my_nbr += 1
                else:
                    sum_percent += 100 * results[2][i] / (self.tests.nr_tests - 1)
                    if results[3] == my_id:
                        my_sum_percent += 100 * results[2][i] / (self.tests.nr_tests - 1)
                        my_errors += 1

            row = get_by_id(test.name)

            if my_nbr > 1:
                more = ('<br><span class="average">Moi : '
                        + (my_sum_percent / (my_nbr + my_errors)).toFixed(1)
                        + '%</span>')
            else:
                more = ''
            row.cells[1].innerHTML += (
                more
                + '<br><span class="average">Tous : '
                + (sum_percent / len(tests)).toFixed(1)
                + '%</span>')

            values.sort()
            if tests[-1][2][i] != self.tests.nr_tests - 1:
                rank = '?'
                percent = 100
            else:
                rank = values.indexOf(tests[-1][0][i]) + 1
                percent = 100 * rank / nbr

            ranks = []
            for results in tests:
                if results[3] == my_id and results[2][i] == self.tests.nr_tests - 1:
                    append(ranks, values.indexOf(results[0][i]) + 1)
            if my_nbr > 1:
                more = (
                    '<br><span class="average">Moi : '
                    + (sum(ranks) / len(ranks)).toFixed(0) + '/' + nbr
                    + '</span><br><span class="average"> </span>')
            else:
                more = ''
            row.cells[2].innerHTML = rank + '/' + nbr + more

            if percent <= 10:
                row.cells[2].style.background = "#0F0"
            elif percent <= 25:
                row.cells[2].style.background = "#8F8"
            elif percent <= 75:
                pass
            else:
                row.cells[2].style.background = "#F88"

            if my_nbr > 1:
                more = ('<br><span class="average">Moi : '
                        + (my_sum_avg / my_nbr / 1000).toFixed(2)
                        + ' s</span>')
            else:
                more = ''

            row.cells[3].innerHTML += (
                more
                + '<br><span class="average">Tous : '
                + (sum_avg / nbr / 1000).toFixed(2)
                + ' s</span>')

            if my_nbr > 1:
                more = ('<br><span class="average">Moi : '
                        + (my_sum_stddev / my_nbr / 1000).toFixed(2)
                        + ' s</span>')
            else:
                more = ''

            row.cells[4].innerHTML += (
                more
                + '<br><span class="average">Tous : '
                + (sum_stddev / nbr / 1000).toFixed(2)
                + ' s</span>')

            row.cells[5].innerHTML = (
                ' <br><span class="average">Moi : ' + my_nbr + "</span><br>"
                + '<span class="average">Tous : ' + nbr + '</span>')

    def order(self):
        """Compute best methods"""
        tests = self.data[self.tests.nr_digits]
        order = {}
        my_order = {}
        nbr = 0
        my_nbr = 0
        my_id = tests[-1][3]
        for results in tests:
            average_method = []
            all_tests_ok = True
            for test in self.tests.phases:
                if not test.name:
                    continue
                if results[2][test.index] != self.tests.nr_tests - 1:
                    all_tests_ok = False
                    break
                append(average_method, [results[0][test.index], test.index])
            if not all_tests_ok:
                continue
            average_method.sort()
            average_method = join([method + ' ' for _, method in average_method[:3]])
            if average_method in order:
                order[average_method] += 1
            else:
                order[average_method] = 1
            if results[3] == my_id:
                my_nbr += 1
                if average_method in my_order:
                    my_order[average_method] += 1
                else:
                    my_order[average_method] = 1
            nbr += 1
        order = [[order[methods], methods] for methods in order]
        order.sort()
        texts = ['<div class="box"><p>Les 3 méthodes les plus rapides (moyenne de ',
                 string(self.tests.nr_tests - 1),
                 ' saisies).<br>',
                 'On ne prend en compte que les ' + nbr + ' tests pour lesquels<br> ',
                 '<b>toutes</b> les méthodes ont atteint 100% de bonnes saisies.<p>'
                 ]
        for nrt, methods in order[::-1][:3]:
            methods = methods.trim().split(' ')
            methods = join([
                '<span style="color:' + COLORS[method] + '">' + METHODS[method] + '</span> '
                for method in methods])
            append(texts, (100 * nrt / nbr).toFixed(0) + '% des tests : ' + methods + '<br>')
        append(texts, '</div>')

        if my_nbr:
            my_order = [[my_order[methods], methods] for methods in my_order]
            my_order.sort()
            append(texts, '<div class="box"><p>Mes 3 méthodes les plus rapides (moyenne sur '
                   + string(my_nbr) + ' parties parfaites).<br>')
            for nrt, methods in my_order[::-1][:3]:
                methods = methods.trim().split(' ')
                methods = join([
                    '<span style="color:' + COLORS[method] + '">' + METHODS[method] + '</span> '
                    for method in methods])
                append(texts, (100 * nrt / my_nbr).toFixed(0) + '% des tests : ' + methods + '<br>')
            append(texts, '</div>')
        else:
            append(texts, '''<div class="box">Vous avez pas encore fait une partie parfaite,
                on n'affiche donc pas le classement de vos méthodes les plus rapides.</div>''')
        document.getElementById('order').innerHTML = join(texts)

    def draw(self, event=None): # pylint: disable=too-many-locals,too-many-branches,too-many-statements
        """Display the current picture"""
        radius = 10

        canvas = get_by_id('canvas')
        canvas.onmousemove = self.draw.bind(self)
        ctx = canvas.getContext("2d")
        tests = self.data[self.tests.nr_digits]
        ctx.lineWidth = 1

        # Search the display transformation

        width = canvas.width
        height = canvas.height
        ctx.fillStyle = "#FFF"
        ctx.fillRect(0, 0, width, height)

        average_max = 0
        stddev_max = 0
        for test in tests:
            for average in test[0]:
                average_max = Math.max(average, average_max)
            for stddev in test[1]:
                stddev_max = Math.max(stddev, stddev_max)
        average_max *= 1.05
        stddev_max *= 1.05
        def X(sec): # pylint: disable=invalid-name
            return width * sec / average_max
        def Y(sec): # pylint: disable=invalid-name
            return height - height * sec / stddev_max

        # Search selected test

        if event:
            cursor_x = X(average_max * (event.layerX - canvas.offsetLeft) / canvas.offsetWidth)
            cursor_y = Y(stddev_max * (1 - (event.layerY - canvas.offsetTop) / canvas.offsetHeight))
            ctx.fillStyle = "#000"
            ctx.beginPath()
            ctx.arc(cursor_x, cursor_y, 3, 0, 2 * Math.PI)
            ctx.fill()
        else:
            cursor_x = cursor_y = -100

        # The axis and tic labels

        ctx.fillStyle = "#000"
        ctx.strokeStyle = "#DDD"
        ctx.font = '18px sans-serif'
        for sec in range(0, int(average_max/1000) + 1):
            x_canvas = X(1000 * sec)
            if sec:
                ctx.fillText(sec + ' secs', x_canvas, height - 40)
            ctx.beginPath()
            ctx.moveTo(x_canvas, 0)
            ctx.lineTo(x_canvas, height)
            ctx.stroke()
        for sec in range(0, int(stddev_max/100) + 1):
            y_canvas = Y(100 * sec)
            if sec:
                ctx.fillText(sec/10 + ' secs', 40, y_canvas)
            ctx.beginPath()
            ctx.moveTo(0, y_canvas)
            ctx.lineTo(width, y_canvas)
            ctx.stroke()

        ctx.font = '32px sans-serif'
        ctx.fillText('Temps moyen des ' + (self.tests.nr_tests - 1) + ' saisies',
                     3 * width / 6, height - 12)
        ctx.rotate(-Math.PI / 2)
        ctx.fillText('Écart-type des ' + (self.tests.nr_tests - 1) + ' saisies',
                     -height/2, 30)
        ctx.rotate(Math.PI / 2)

        # Draw discs

        selected_test = tests[-1]
        for test in tests:
            for i, color in enumerate(COLORS):
                if test[2][i] == (self.tests.nr_tests - 1):
                    x_canvas = X(test[0][i])
                    y_canvas = Y(test[1][i])
                    ctx.fillStyle = color + '8'
                    ctx.beginPath()
                    ctx.arc(x_canvas, y_canvas, radius, 0, 2 * Math.PI)
                    ctx.fill()

                    if (x_canvas - cursor_x)**2 + (y_canvas - cursor_y)**2 <= radius * radius:
                        selected_test = test

        # The disc borders for the selected user

        ctx.strokeStyle = "#000"
        ctx.lineWidth = 1
        ctx.setLineDash([5, 5])
        for method in self.tests.phases:
            method.stats_ip = [0, 0, 0]
        for test in tests:
            if test[3] != selected_test[3]:
                continue
            for method in self.tests.phases:
                i = method.index
                average = test[0][i]
                if average:
                    ctx.beginPath()
                    x_canvas = X(average)
                    y_canvas = Y(test[1][i])
                    ctx.arc(x_canvas, y_canvas, radius, 0, 2 * Math.PI)
                    ctx.stroke()
                    method.stats_ip[0] += 1
                    method.stats_ip[1] += average
                    method.stats_ip[2] += test[1][i]
        ctx.setLineDash([])

        # Display stats for the ip
        ctx.fillStyle = '#000'
        ctx.font = '32px sans-serif'
        ctx.fillText("Moyenne et écart-type des tests entourés :", 150, 30)

        for method in self.tests.phases:
            if not method.name:
                continue
            if method.stats_ip[0] == 0:
                message = 'Pas de stats'
            else:
                message = (
                    (method.stats_ip[1]/method.stats_ip[0]/1000).toFixed(2)
                    + ' ' + (method.stats_ip[2]/method.stats_ip[0]/1000).toFixed(2))
            ctx.fillStyle = method.color
            ctx.fillText(method.name + ' ' + message,
                         150, 80 + 45 * method.index)

        # The disc borders for the selected test

        ctx.lineWidth = 2
        for test in self.tests.phases:
            average = selected_test[0][test.index]
            stddev = selected_test[1][test.index]
            if not average:
                continue
            ctx.beginPath()
            ctx.arc(X(average), Y(stddev), radius, 0, 2 * Math.PI)
            ctx.stroke()

#############################################################################
#############################################################################
# A set of tests
#############################################################################
#############################################################################

COLORS = []
METHODS = []
for _method, _color in [
        # ('Keypad', '#F00'),
        # ('Keyboard', '#0F0'),
        ('KeyboardText', '#0F0'),
        # ('Buttons10', '#F0F'),
        # ('Buttons20', '#0FF'),
        # ('Buttons40', '#88F'),
        ('ButtonsText10', '#F0F'),
        ('ButtonsText20', '#0FF'),
        ('ButtonsText40', '#88F'),
    ]:
    append(COLORS, _color)
    append(METHODS, _method)

class Tests:
    """Launch the tests"""
    nr_tests = 10 # Number of test to do for each phase
    nr_digits = 3 # Number of digits of the numbers
    xhr = None
    stats = None
    def __init__(self):
        self.debug = 'debug' in string(window.location)
        self.i = -1
        self.phases = [Welcome(self)]
        for i, method in enumerate(METHODS):
            append(self.phases, eval('new ' + method + '(self)')) # pylint: disable=eval-used
            self.phases[-1].color = COLORS[i]
            self.phases[-1].index = i
        append(self.phases, End(self))
        if self.debug:
            self.i = len(self.phases) - 2
            for test in self.phases:
                if test.name:
                    test.times = [1000 + 2 * random_int(3) for _ in range(self.nr_tests)]
                if test.index == 1:
                    test.times[1] *= -1
        self.done()
    def done(self):
        """Start the next test"""
        self.i += 1
        self.phases[self.i].start()
    def record(self):
        """Record the stats on the server"""
        @external
        class XMLHttpRequest: # pylint: disable=too-few-public-methods
            """Fake to please pylint"""
            onload = lambda: None
        self.xhr = XMLHttpRequest()
        self.xhr.open('POST', window.location.toString() + millisec(), True)
        self.xhr.overrideMimeType("text/plain; charset=UTF-8")
        self.xhr.onload = self.record_done.bind(self)
        if self.debug:
            self.xhr.send('')
        else:
            self.xhr.send(self.json())

    def record_done(self):
        """The data have been recorded, get the statistics"""
        self.stats = Stats(self.xhr.responseText, self)
        if self.debug:
            self.phases[self.i].page.innerHTML = self.resume() + self.stats.html()
        else:
            self.phases[self.i].page.innerHTML += self.stats.html()
        self.stats.update_rank()
        self.stats.order()

    def resume(self):
        """A resume table in HTML"""
        stats = [
            '<div class="box">',
            '<p>Saisie de ', string(self.nr_tests), ' valeurs comportant ',
            string(self.nr_digits), ' caractères.<br>',
            "Mes résultats pour cette partie et les moyennes en petit.",
            '''<table><tr>
            <td style="text-align:center; width:10em">La première saisie<br>n'est pas comptée
            <th>Bonnes<br>saisies
            <th>Rang
            <th>Temps<br>moyen
            <th>Écart-<br>type
            <th>Nbr de<br>parties
            </tr>'''
            ]
        for test in self.phases:
            if test.name:
                infos = test.stats()
                append(stats, '<tr id="')
                append(stats, test.name)
                append(stats, '"><th style="color:' + test.color + '">')
                append(stats, test.name + ' ' + test.icon)
                percent = int(100 * infos[1] / infos[0])
                if percent == 100:
                    append(stats, "<td>")
                else:
                    append(stats, '<td style="background: #F88">')
                append(stats, percent)
                append(stats, '%<td>?<td>')
                append(stats, (infos[2]/1000).toFixed(2))
                append(stats, " s<td>")
                append(stats, (infos[3]/1000).toFixed(2))
                append(stats, " s<td>?</tr>")
        append(stats, '</table></div><div id="order"></div>')
        return join(stats)

    def json(self):
        """Generate the data to record"""
        return JSON.stringify({
            'nr_tests': self.nr_tests,
            'nr_digits': self.nr_digits,
            'tests': [
                [test.name, test.times]
                for test in self.phases
                if test.name
            ]
        })
